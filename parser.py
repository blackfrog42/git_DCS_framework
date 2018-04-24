import argparse
import utils


parser = argparse.ArgumentParser(description='Render a LaTex Template with variables.')

parser.add_argument('type', choices=['tex', 'options', 'json'])
parser.add_argument('-i','--input', help='Input File', required=False, default='./example.txt' )
parser.add_argument('-t','--template', help='Template File', required=False, default='./template.tex')
parser.add_argument('-r','--renderfile', help='Save Render to File', required=False, default='./rendered_latex.tex')

args = vars(parser.parse_args())


project = "./"
in_file = args['input']
build_d = "{}.build/".format(project)
template_file = args['template']
out_file = "{}renderer_template.pdf".format(project)


#print("options = {}").format(options)
#TODO re-enable other data formats using arg parse switch https://stackoverflow.com/questions/17909294/python-argparse-mutual-exclusive-group


template = utils.get_template(template_file)

if args['type'] == "json":
    options = utils.get_json_options_recursively(in_file)
    print()
elif args['type'] == "options":
    options = utils.get_options_from_file(in_file)
else: # args['type'] == "tex":
    options = dict()

utils.compile_pdf_from_template(template, options, out_file)

