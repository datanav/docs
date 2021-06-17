#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import shutil
import os

def split_training_into_topics(root_level_header, files, output_folder, rename_ref_prefix):
    """
    I use the functions within me to split RST files into a file for each
    root level header in the file.
    """

    def find_root_headers(file):
        """
        I'm a function which finds all the root level headers in a document.
        Root level header character can be set at the top variable.
        """
        lines = open(file).readlines()
        cur_ref = None
        tmp_cur_ref = None
        prev_line = None
        returnlist = []
        for l in lines:
            l = l.replace('\n', '')
            if l.startswith('.. _') and l.endswith(':'):
                tmp_cur_ref = l
            linelength = len(l)
            reflength = 0
            for c in l:
                if c == root_level_header:
                    reflength += 1
            if linelength == reflength and linelength != 0:
                cur_ref = tmp_cur_ref
                returnlist.append({
                    "reference": cur_ref,
                    "title": prev_line,
                    "source_file": file
                })
            prev_line = l


        return returnlist

    def createFiles(file, splitonthis: list):
        """
        I'm a function which a splits a string on a list of strings.
        I make sure that there is no overlap in the output strings.
        """
        mainfile = open(file).read()
        splitonthis.reverse()
        for x, e in enumerate(splitonthis):
            splitted_main_file = mainfile.split(e['reference'])
            if splitted_main_file:
                mainfile = splitted_main_file[0]
            ref_name = f".. _{e['reference'][4:]}"
            e['text'] = ref_name + splitted_main_file[-1]
        splitonthis.reverse()
        return splitonthis

    total_topics = []
    for f in files:
        filenameSplitted = f.split('/')[-2:]
        topics = find_root_headers(f)
        from json import dumps
        file = open(f).read()
        total_topics += createFiles(file=f, splitonthis=topics)

    return total_topics

def get_courses(folder):
    output = []
    for course_name in [e[0:-4] for e in os.listdir(folder) if e.endswith('.rst')]:
        curpath = os.path.join(folder, f'{course_name}.rst')
        output.append({"course_name": course_name, "course_file_path": curpath})
    return output

def replace_course_file_content(course, rename_ref_prefix, topics):
    with open(course["course_file_path"], 'r+') as f:
        content = f.readlines()
        newfile = ""
        for line in content:
            curRef = None
            curLine = line
            if line.startswith('   ###') and line.endswith('###\n'):
                curRef = line[6:-4]
                found = False
                for t in topics:
                    if t["reference"] == curRef:
                        found = True
                        curLine = t['text']
                        topic_media_folder = f'{"/".join(t["source_file"].split("/")[0:-1])}/media/'
                        curLine = curLine.replace('.. figure:: ./media/', f'.. figure:: {topic_media_folder}')
                        break
                if found == False:
                    raise Exception(f'Could not find reference {curRef} in training docs!')
            curLine = curLine.replace('.. _', f'.. _{rename_ref_prefix}')
            newfile += curLine
        f.close()
        return course, newfile

def create_course_files(new_course_files, directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)
    for course_info, file_content in new_course_files:
        newfile_path = os.path.join(directory, f'{course_info["course_name"]}.rst')
        with open(newfile_path, 'w') as newfile:
            newfile.write(file_content)
            newfile.close()

#files = ["training/010_architecture_and_concepts/020_Beginner.rst"]

def create_courses(files, output_folder, courses_path, root_level_header, rename_ref_prefix):

    output_folder_full_path = os.path.join(pathlib.Path().absolute(), output_folder)
    courses_path_full = os.path.join(pathlib.Path().absolute(), COURSES_PATH)
    topics = split_training_into_topics(root_level_header, files, output_folder, rename_ref_prefix)
    courses = get_courses(courses_path_full)
    new_course_files = []
    for course in courses:
        new_course_files.append(replace_course_file_content(course, rename_ref_prefix, topics))
    create_course_files(new_course_files, output_folder_full_path)

if __name__ == '__main__':
    files = ["training/010_architecture_and_concepts/020_Beginner.rst","training/010_architecture_and_concepts/030_Novice.rst","training/010_architecture_and_concepts/040_Intermediate.rst","training/010_architecture_and_concepts/050_Advanced.rst","training/010_architecture_and_concepts/060_Epilogue.rst","training/010_architecture_and_concepts/architecture_and_concepts.rst","training/020_systems/020_Beginner.rst","training/020_systems/030_Novice.rst","training/020_systems/040_Intermediate.rst","training/020_systems/060_Epilogue.rst","training/020_systems/systems.rst","training/030_dtl/020_Beginner.rst","training/030_dtl/030_Novice.rst","training/030_dtl/040_Intermediate.rst","training/030_dtl/050_Advanced.rst","training/030_dtl/060_Epilogue.rst","training/030_dtl/dtl.rst","training/040_projects_and_infrastructure/020_Beginner.rst","training/040_projects_and_infrastructure/030_Novice.rst","training/040_projects_and_infrastructure/040_Intermediate.rst","training/040_projects_and_infrastructure/060_Epilogue.rst","training/040_projects_and_infrastructure/projects_and_infrastructure.rst","training/050_microservices/020_Beginner.rst","training/050_microservices/030_Novice.rst","training/050_microservices/040_Intermediate.rst","training/050_microservices/050_Advanced.rst","training/050_microservices/060_Epilogue.rst","training/050_microservices/microservices.rst","training/060_sesam_in_the_wild/020_Beginner.rst","training/060_sesam_in_the_wild/030_Novice.rst","training/060_sesam_in_the_wild/040_Intermediate.rst","training/060_sesam_in_the_wild/050_Advanced.rst","training/060_sesam_in_the_wild/060_Epilogue.rst","training/060_sesam_in_the_wild/sesam_in_the_wild.rst"]
    output_folder = 'training/courses/tmp'
    root_level_header = '~'
    rename_ref_prefix = 'tc_'
    COURSES_PATH = 'training/courses'
    create_courses(files, output_folder, COURSES_PATH, root_level_header, rename_ref_prefix)
