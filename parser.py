import argparse
import utils


parser = argparse.ArgumentParser(description='Render a LaTex Template with variables.')

#parser.add_argument('-i','--in', help='Input File', required=False, default='./example.txt' )
parser.add_argument('-t','--template', help='Template File', required=False, default='./template.tex')
parser.add_argument('-j','--json', help='JSON Data File', required=False, default='./data.json')
parser.add_argument('-r','--renderfile', help='Save Render to File', required=False, default='./rendered_latex.tex')

args = vars(parser.parse_args())


project = "./"
in_file = args['json']
build_d = "{}.build/".format(project)
template_file = args['template']
out_file = "{}renderer_template.pdf".format(project)

#options = utils.get_options_from_file(in_file)
#print("options = {}").format(options)
#TODO re-enable other data formats using arg parse switch https://stackoverflow.com/questions/17909294/python-argparse-mutual-exclusive-group


options =  utils.get_options_from_json_file(in_file)


template = utils.get_template(template_file)

renderer_template = template.render(**options)
with open(args['renderfile'],"w") as file:
	file.write(renderer_template)
	file.write(str(options))


utils.compile_pdf_from_template(template, options, out_file)

