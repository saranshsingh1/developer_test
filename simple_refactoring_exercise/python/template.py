def template(source_template, req_id):

    template  = str(source_template)

    code = str(req_id)
    altcode = code[0:5] + "-" + code[5:8]

    return template.format(CODE = code, ALTCODE = altcode)
