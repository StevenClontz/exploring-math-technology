from lxml import etree
import os
from shutil import copytree
import click
import subprocess
import time


def make_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


@click.command()
def build():
    book = etree.parse("source/main.ptx")
    book.xinclude()
    xsl = etree.parse("xsl/jupyter.xsl")
    transform = etree.XSLT(xsl)
    make_directory("output")
    jo_directory = "output/jupyter-"+str(time.time())
    jo_directory_team = jo_directory+"/team"
    jo_directory_indv = jo_directory+"/individual"
    make_directory(jo_directory)
    make_directory(jo_directory_team)
    make_directory(jo_directory_indv)
    for cindex, chapter in enumerate(book.xpath("//chapter"), start=1):
        if chapter.xpath("@xml:id"):
            jo_directory_team_ch = jo_directory_team + "/chapter-" + str(cindex) + "-" + chapter.xpath('./@xml:id')[0]
            jo_directory_indv_ch = jo_directory_indv + "/chapter-" + str(cindex) + "-" + chapter.xpath('./@xml:id')[0]
            make_directory(jo_directory_team_ch)
            make_directory(jo_directory_indv_ch)
            for sindex, section in enumerate(chapter.xpath("section"), start=1):
                if section.xpath("@xml:id"):
                    team_section_path = jo_directory_team_ch +"/section-" + str(cindex) + "-" + str(
                        sindex) + "-" + section.xpath('./@xml:id')[0] + ".ipynb"
                    indv_section_path = jo_directory_indv_ch +"/section-" + str(cindex) + "-" + str(
                        sindex) + "-" + section.xpath('./@xml:id')[0] + ".ipynb"
                    section_code = "'" + str(cindex) + "." + str(sindex) + "'"
                    transform(
                        section,
                        section=section_code,
                        mode="'team'").write_output(team_section_path)
                    transform(
                        section,
                        section=section_code,
                        mode="'individual'").write_output(indv_section_path)
    #if not os.path.exists("activities/images"):
    #  copytree("apc/src/images","activities/images")
    subprocess.run(['pretext','build'])


if __name__ == '__main__':
    build()
