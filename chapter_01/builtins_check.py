import builtins
print(dir(builtins))
print(len(dir(builtins)))

callable_builtins=[f for f in dir(builtins) if callable(getattr(builtins,f))]
print(callable_builtins)
print(len(callable_builtins))