"""Builds the wiki pages from the repository's README files.

Home comes from README.md, and every app folder with a README.md becomes its own
page, named after the guide's title ("Red Alert Israel for Homey" becomes "Red-Alert-Israel"). Links to app guides point to their
wiki pages, other relative links to the files on GitHub. Pages written here are
overwritten on every run: edit the README files, not the wiki.

Usage: python3 sync_wiki.py <repository root> <wiki checkout> <owner/repo> [branch]
"""
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

LINK = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)\)')


def page_name(folder, text):
    """Page name from the guide's title without "for Homey": "Switcher for Homey" gives "Switcher"."""
    match = re.search(r'^#\s+(.+)$', text, re.M)
    title = match.group(1).strip() if match else folder.replace('-', ' ').title()
    title = re.sub(r'\s+for Homey$', '', title)
    return re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-')


def rewrite_links(text, source_dir, repo, branch, pages):
    base = f'https://github.com/{repo}/blob/{branch}/{source_dir + "/" if source_dir else ""}'

    def replace(match):
        label, target = match.groups()
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            return match.group(0)
        path, _, anchor = target.partition('#')
        folder = Path(source_dir, path).parent.as_posix() if path.endswith('README.md') else None
        if folder in pages:
            return f'[{label}]({pages[folder]}{"#" + anchor if anchor else ""})'
        return f'[{label}]({urljoin(base, target)})'

    return LINK.sub(replace, text)


def notice(source, repo, branch):
    url = f'https://github.com/{repo}/blob/{branch}/{source}'
    return f'\n\n---\n\n_This page is generated from [{source}]({url}). Edit that file; changes here are overwritten._\n'


def main(root, wiki, repo, branch='main'):
    root, wiki = Path(root), Path(wiki)
    apps = sorted(p.parent.name for p in root.glob('*/README.md'))
    texts = {folder: (root / folder / 'README.md').read_text(encoding='utf-8') for folder in apps}
    pages = {folder: page_name(folder, texts[folder]) for folder in apps}

    def title_of(text, fallback):
        match = re.search(r'^#\s+(.+)$', text, re.M)
        return match.group(1).strip() if match else fallback

    written = {}
    home = (root / 'README.md').read_text(encoding='utf-8')
    written['Home.md'] = rewrite_links(home, '', repo, branch, pages) + notice('README.md', repo, branch)

    sidebar = ['**[Home](Home)**', '']
    for folder in apps:
        text = texts[folder]
        written[f'{pages[folder]}.md'] = rewrite_links(text, folder, repo, branch, pages) + notice(f'{folder}/README.md', repo, branch)
        sidebar.append(f'- [{title_of(text, pages[folder])}]({pages[folder]})')
    sidebar += ['', f'[Report a problem](https://github.com/{repo}/issues/new/choose)']
    written['_Sidebar.md'] = '\n'.join(sidebar) + '\n'

    for name, content in written.items():
        (wiki / name).write_text(content, encoding='utf-8')
        print(f'wrote {name}')


if __name__ == '__main__':
    main(*sys.argv[1:])
