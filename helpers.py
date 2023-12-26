def window(lt, size=2):
    if len(lt) == 0:
        return None
    if not (isinstance(lt, list) or isinstance(lt, tuple)):
        raise ValueError(f'Cannot window object of type {type(lt)}')

    for i in range(len(lt) - size + 1):
        yield lt[i:i + size]
