import web

urls = (
    '/delete', 'mvc.controllers.delete.Delete',
    '/', 'mvc.controllers.index.Index',
    '/insert', 'mvc.controllers.insert.Insert',
    '/list', 'mvc.controllers.list.List',
    '/update', 'mvc.controllers.update.Update',
    '/view', 'mvc.controllers.view.View',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 8888))
    app.run()
   
