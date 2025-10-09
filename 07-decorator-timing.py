from  datetime import datetime
from functools import wraps
from statistics import mean, stdev
from typing import Callable, ParamSpec, TypeVar, overload

# avant python 3.12:
# P = ParamSpec('P')
# T = TypeVar('T')
# def timing(f: Callable[P, T] | None= None, /, *, n: int = 1)

# en python 3.12+, introduction des variables TypeVar, ParamSpec et TypeVarTuple au niveau de la fonction

@overload
def timing[**P, T](f: Callable[P, T], /, *, n: int = 1) -> Callable[P, T]: ...

@overload
def timing[**P, T](f: None = None, /, *, n: int = 1) -> Callable[[Callable[P, T]], Callable[P, T]]: ...

def timing[**P, T](f: Callable[P, T] | None= None, /, *, n: int = 1) -> \
    Callable[P, T] | Callable[[Callable[P, T]], Callable[P, T]]:
    
    def decorator(f: Callable[P, T]) -> Callable[P, T]:
    
        @wraps(f)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            durations = []
            result: T | None = None
            for _ in range(n):
                dt1 = datetime.now()
                result = f(*args, **kwargs)
                dt2 = datetime.now()
                delta = dt2 - dt1
                durations.append(delta.total_seconds()) 

            assert result is not None, "n > 0 guarantees result is defined"

            avg = mean(durations)
            std = stdev(durations) if n > 1 else 0.0
            print(f"Executed {n} times. Avg: {avg:.6f}s | Std Dev: {std:.6f}s")
            return result
        
        return wrapper
    
    if n <= 0:
        raise ValueError(f"n must be strictly positive, got {n}")
    
    # gestion du decorator appelé 
    #   directement avec la fonction: @timing 
    #   ou avec ses paramètres: @timing() ou @timing(n=10)    
    if f is not None:
        return decorator(f)
    else:
        return decorator
    
@timing(n=10)
def super_computation(a, b, c, /, *, d=3, e=True, **kwargs):
    res = (a + b + c) * (d if e else -d) 
    if 'coef' in kwargs:
        res *= kwargs['coef']
    return res

super_computation(1, 2, 3, d=5, coef=0.9, dummy='dumber', e=False)

@timing()
def super_computation2(a: float, b: float, c: float, /, *, d: float = 3.0, e: bool = True, **kwargs) -> float:
    res = (a + b + c) * (d if e else -d) 
    if 'coef' in kwargs:
        res *= kwargs['coef']
    return res

super_computation2(1, 2, 3, d=5, coef=0.9, dummy='dumber', e=False)

@timing
def super_computation3(a: float, b: float, c: float, /, *, d: float = 3.0, e: bool = True, **kwargs) -> float:
    res = (a + b + c) * (d if e else -d) 
    if 'coef' in kwargs:
        res *= kwargs['coef']
    return res

super_computation3(1, 2, 3, d=5, coef=0.9, dummy='dumber', e=False)