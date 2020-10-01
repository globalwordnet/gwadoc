
# thanks: http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
# thanks: http://flask.pocoo.org/snippets/55/

import sys

from pathlib import Path
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
import os.path
import argparse
import re

import docutils.core
import jinja2


sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))
import gwadoc
#gwadoc.set_preferred_language('en')


DIR = Path(__file__).parent.resolve()


def rst_renderer(fmt):
    """Create a function to render ReStructuredText to *fmt*."""

    @jinja2.evalcontextfilter
    def render_rst(eval_ctx, s):
        s = docutils.core.publish_parts(str(s), writer_name=fmt)['body']
        s = s.strip()
        # remove (hopefully) unnecessary <p>...</p>
        if s[:3] == '<p>' and s[-4:] == '</p>':
            s = s[3:-4]
        # replace ILIURL with the actual URL
        s = s.replace('ILIURL', 'https://lr.soh.ntu.edu.sg/omw/omw/concepts/ili')
        # make sure Jinja2 doesn't try to escape the HTML markup
        if eval_ctx.autoescape:
            s = jinja2.Markup(s)
        return s

    return render_rst


def build(args):
    gwadoc.set_preferred_language(args.lang)
    loader =  jinja2.FileSystemLoader(DIR / 'templates')

    if args.format == 'html':
        env = jinja2.Environment(
            loader=loader,
            autoescape=jinja2.select_autoescape(['html', 'xml']))
        env.filters['render_rst'] = rst_renderer('html')
        template = env.get_template('index.html')

    elif args.format == 'latex':
        LATEX_SUBS = (
            (re.compile(r'\\'), r'\\textbackslash'),
            (re.compile(r'([{}_#%&$])'), r'\\\1'),
            (re.compile(r'~'), r'\~{}'),
            (re.compile(r'\^'), r'\^{}'),
            (re.compile(r'"'), r"''"),
            (re.compile(r'\.\.\.+'), r'\\ldots'),
        )
        def escape_tex(value):
            newval = value
            for pattern, replacement in LATEX_SUBS:
                newval = pattern.sub(replacement, newval)
            return newval
        env = jinja2.Environment(
            block_start_string=r'\BLOCK{',
            block_end_string='}',
            variable_start_string=r'\VAR{',
            variable_end_string='}',
            comment_start_string=r'\%{',
            comment_end_string=r'}',
            line_statement_prefix=r'\STMT',
            line_comment_prefix=r'\CMNT',
            trim_blocks=True,
            autoescape=False,
            loader=loader)
        env.filters['render_rst'] = rst_renderer
        env.filters['escape_tex'] = escape_tex
        template = env.get_template('index.tex')

    else:
        raise ValueError('invalid format: {}'.format(args.format))

    print(template.render(gwadoc=gwadoc))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('format', choices=('html', 'latex'), default='html')
    parser.add_argument("--lang", help="language to make the docs in", default="en")
    args = parser.parse_args()
    build(args)

