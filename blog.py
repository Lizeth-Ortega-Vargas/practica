""" Basic blog using webpy 0.3 """
import web
import model


urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
)


t_globals = {
    'datestr': web.datestr
}

render=web.template.render('templates', base='base', globals=t_globals)

web.config.debug=False


class Index:

    def GET(self):
        """ mostrar la pagina """
        posts = model.get_posts()
        return render.index(posts)

 
class View:

    def GET(self, id):
        """ Ver un producto """
        post = model.get_post(int(id))
        return render.view(post)


class New:

    form = web.form.Form(
        web.form.Textbox('nombre', web.form.notnull, 
            description="nombre:"),
        web.form.Textbox('apellidos', web.form.notnull, 
            description="apellidos:"),
        web.form.Textbox('sexo', web.form.notnull, 
            description="sexo:"),
        web.form.Textbox('curp', web.form.notnull, 
            description="curp:"),
        web.form.Button('Enviar'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)


class Delete:

    def POST(self, id):
        id_alumno=int(id)
        model.del_post(id_alumno)
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        id_alumno=int(id)
        post = model.get_post(id_alumno)
        form = New.form()
        form.fill(post)
        return render.edit(post, form)


    def POST(self, id):
        id_alumno=int(id)
        form = New.form()
        post = model.get_post(id_alumno)
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.nombre, form.d.apellidos, form.d.sexo, form.d.curp)
        raise web.seeother('/')

app = web.application(urls, globals())


if __name__ == '__main__':
     app.run()