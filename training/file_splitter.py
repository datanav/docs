import os
import pathlib
import shutil

def split_rst_file_root_level(root_level_header, files, output_folder, rename_ref_prefix):
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
                    "title": prev_line
                })
                #print(f'#\n{cur_ref}\n\n{prev_line}\n{l}\n#')
            prev_line = l


        return returnlist

    def createFiles(file, splitonthis: list):
        """
        I'm a function which a splits a string on a list of strings.
        I make sure that there is no overlap in the output strings.
        """
        mainfile = open(file).read()
        createfiles = []
        splitonthis.reverse()
        for x, e in enumerate(splitonthis):
            splitted_main_file = mainfile.split(e['reference'])
            ref_name = f".. _{rename_ref_prefix}{e['reference'][4:]}"
            createfiles.append(ref_name + splitted_main_file[-1])
            if splitted_main_file:
                mainfile = splitted_main_file[0]
        createfiles.reverse()
        return createfiles

    def writeFiles(writingFiles: list, file_prefix):
        """
        I'm a simple function which writes a rst files.
        I create a file named after the first line for each file provided.
        I suffix the filename with '.rst'
        """
        for wf in writingFiles:
            filename = wf.split('\n')[0][4:-1] + '.rst'
            curfile = open(f'{output_folder}/{file_prefix}{filename}', 'w')
            curfile.write(wf)
            curfile.close()

    fullpath = os.path.join(pathlib.Path().absolute(), output_folder)
    if os.path.exists(fullpath):
        shutil.rmtree(fullpath)
    os.makedirs(fullpath)
    for f in files:
        filenameSplitted = f.split('/')
        file_prefix = f'{filenameSplitted[0][4:]}_{filenameSplitted[1][4:-4]}_'
        splitonthis = find_root_headers(f)
        file = open(f).read()
        writeFiles(createFiles(file=f, splitonthis=splitonthis), file_prefix=file_prefix)

files = ["training/010_architecture_and_concepts/020_Beginner.rst","training/010_architecture_and_concepts/030_Novice.rst","training/010_architecture_and_concepts/040_Intermediate.rst","training/010_architecture_and_concepts/050_Advanced.rst","training/010_architecture_and_concepts/060_Epilogue.rst","training/010_architecture_and_concepts/architecture_and_concepts.rst","training/020_systems/020_Beginner.rst","training/020_systems/030_Novice.rst","training/020_systems/040_Intermediate.rst","training/020_systems/060_Epilogue.rst","training/020_systems/systems.rst","training/030_dtl/020_Beginner.rst","training/030_dtl/030_Novice.rst","training/030_dtl/040_Intermediate.rst","training/030_dtl/050_Advanced.rst","training/030_dtl/060_Epilogue.rst","training/030_dtl/dtl.rst","training/040_projects_and_infrastructure/020_Beginner.rst","training/040_projects_and_infrastructure/030_Novice.rst","training/040_projects_and_infrastructure/040_Intermediate.rst","training/040_projects_and_infrastructure/060_Epilogue.rst","training/040_projects_and_infrastructure/projects_and_infrastructure.rst","training/050_microservices/020_Beginner.rst","training/050_microservices/030_Novice.rst","training/050_microservices/040_Intermediate.rst","training/050_microservices/050_Advanced.rst","training/050_microservices/060_Epilogue.rst","training/050_microservices/microservices.rst","training/060_sesam_in_the_wild/020_Beginner.rst","training/060_sesam_in_the_wild/030_Novice.rst","training/060_sesam_in_the_wild/040_Intermediate.rst","training/060_sesam_in_the_wild/050_Advanced.rst","training/060_sesam_in_the_wild/060_Epilogue.rst","training/060_sesam_in_the_wild/sesam_in_the_wild.rst"]
output_folder = 'tmp'
root_level_header = '~'
rename_ref_prefix = 'training_courses_'
split_rst_file_root_level(root_level_header, files, output_folder, rename_ref_prefix)
