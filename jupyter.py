from lxml import etree
import os
from shutil import copytree
import click


def make_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


@click.command()
@click.option('--previews/--no-previews',
              default=True,
              help='Include preview activities for each section.')
def build(previews):
    include_previews = "'yes'" if previews else "'no'"
    book = etree.parse("source/main.ptx")
    book.xinclude()
    xsl = etree.parse("xsl/jupyter.xsl")
    transform = etree.XSLT(xsl)
    make_directory("output")
    make_directory("output/jupyter")
    for cindex, chapter in enumerate(book.xpath("//chapter"), start=1):
        for sindex, section in enumerate(chapter.xpath("section"), start=1):
            section_path = "output/jupyter/section-" + str(cindex) + "-" + str(
                sindex) + "-" + section.xpath('./@xml:id')[0] + ".ipynb"
            section_code = "'" + str(cindex) + "." + str(sindex) + "'"
            transform(
                section,
                section=section_code,
                includepreviews=include_previews).write_output(section_path)
    #if not os.path.exists("activities/images"):
    #  copytree("apc/src/images","activities/images")


if __name__ == '__main__':
    build()