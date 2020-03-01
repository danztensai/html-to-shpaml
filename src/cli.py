import manager
from bs4 import BeautifulSoup
from bs4.element import Comment

manager = manager.Manager()
SPACER = '    '

class HtmlTag:
    def __init__(self, tag_name: str, attr_dic: {}, elem, indentation=None):
        self.tag_name = tag_name
        self.attr_dic = attr_dic
        self.contents = elem.contents
        self.elem = elem
        self.indentation = indentation if indentation is not None else ''

    def _shpaml_tag(self):
        classes = ''
        try:
            classes = "".join(
                [f".{class_name}" for class_name in self.attr_dic['class']])
        except Exception:
            pass

        attr_lis = []
        for k, v in self.attr_dic.items():
            if k == 'class':
                continue
            attr_lis += [f'{k}="{add_slashes(v)}"']
        attrs = " ".join(attr_lis)

        has_content = self._has_contents()
        double_stroke = "||" if not has_content else ''

        this_tag = f"{self.indentation}{self.tag_name}{classes} {attrs} {double_stroke}".rstrip()
        return this_tag

    def _has_contents(self):
        try: str_nodes = list(filter(lambda x: len(x.strip()) > 0, self.contents))
        except Exception: return True

        return len(str_nodes) > 0

    def to_shpaml(self):
        lines = [self._shpaml_tag()] + HtmlTag.parse_contents(self.contents, self.indentation + SPACER)
        return lines

    @staticmethod
    def parse_contents(contents, indentation):
        lis = []
        for content in contents:
            if hasattr(content, 'name') and content.name is not None:
                tag = HtmlTag(content.name, content.attrs, content, indentation)
                lis += tag.to_shpaml()
                continue

            if len(content.strip()) > 0:
                lis += [f'{indentation} {content.strip()}']
        return lis


@manager.command
def convert(path_to_html):
    """
    Parses a html file and outputs it's equivalent in shpaml
    """
    with open(path_to_html, 'r') as f:
        html_text = f.read()
        soup = BeautifulSoup(html_text, 'html.parser')
        soup = _rm_comments_from_soup(soup)
        root = soup.contents[0]
        tag = HtmlTag(root.name, root.attrs, root)
        return "\n".join(tag.to_shpaml())


def _rm_comments_from_soup(soup):
    comments = soup.find_all(text=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()
    return soup

def add_slashes(s):
    l = ["\\", '"', "'", "\0", ]
    for i in l:
        if i in s:
            s = s.replace(i, '\\'+i)
    return s


if __name__ == '__main__':
    manager.main()
