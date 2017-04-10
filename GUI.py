def GUIstart():
    import htmlPy
    import os

    Base_dir = os.path.abspath(os.path.dirname(__file__))

    app = htmlPy.AppGUI(title=u"optimal job", maximized=True, plugins=True)

    app.static_path = os.path.join(Base_dir,"static")
    app.template_path = os.path.join(Base_dir,"template")

    app.web_app.setMinimumWidth(1000)
    app.web_app.setMinimumHeight(790)


