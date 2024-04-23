class introspection_info:
    def __init__(self, obj):
        self.obj = obj


introspection = introspection_info(23)

print(type(introspection), dir(introspection), isinstance(introspection, introspection_info))
