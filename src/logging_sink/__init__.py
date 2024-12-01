def logging_func(f, *args, **kwargs):
    """Demo logging decorator.

    This could do absolutely anything.
    """

    if f is None:
        print(f'* DAG EXECUTE {args} {kwargs}')
        return

    def wrapper(*args, **kwargs):
        print(f'* BLOCK BEGIN EXECUTE: {f} {args} {kwargs}')
        for k in list(kwargs.keys()):
            # Remove logging arguments.
            #
            if k.startswith('sier2') and k.endswith('_'):
                del kwargs[k]

        r = f(*args, **kwargs)
        print(f'* BLOCK END  EXECUTE: {f} {args} {kwargs}')

        return r

    return wrapper
