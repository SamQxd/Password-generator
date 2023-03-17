from main import window, initial_values, service_class, password_class, generator_class, new_window_class

service_class = service_class(window.root, initial_values.password_generator_list)
password_class = password_class(window.root)
generator_class = generator_class(window.root, initial_values.password_symbols, initial_values.password_database)
new_window_class = new_window_class(window.root)

service_class.service()
password_class.password()
generator_class.password_generator()

window.root.mainloop()