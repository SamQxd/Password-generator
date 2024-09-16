from main import service_class, window, initial_values, password_class, generator_class

service_class = service_class(window.root, initial_values.password_generator_list)
password_class = password_class(window.root)
generator_class = generator_class(window.root, initial_values.password_symbols)

service_class.service()
password_class.password()
generator_class.password_generator()

window.root.mainloop()