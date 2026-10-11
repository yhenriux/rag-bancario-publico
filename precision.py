"""Precisão ilustrativa, fixada antes da geração final; sem simular evidência bancária."""
import random
from math import ceil, sqrt
from statistics import NormalDist, mean, median
from study import write


def simulate(n, q, repetitions=2000, seed=2026):
    rng=random.Random(seed);widths=[];coverage=[]
    z=NormalDist().inv_cdf(.975)
    for _ in range(repetitions):
        pairs=[]
        for _ in range(n):
            u=rng.random();pairs.append(1 if u<q/2 else -1 if u<q else 0)
        delta=mean(pairs)
        variance=sum((p-delta)**2 for p in pairs)/(n-1)
        half=z*sqrt(variance/n);widths.append(half);coverage.append(abs(delta)<=half)
    return {'independent_pairs':n,'discordance':q,'assumed_difference':0,
       'simulations':repetitions,'seed':seed,'median_normal_ci95_half_width':median(widths),
       'simulated_normal_ci95_coverage_at_zero':mean(coverage),
       'warning':'Ilustração independente. Não é intervalo do experimento nem corrige referência assistida ou seleção.'}


def report():
    nd=NormalDist();q=.25;delta=.10;alpha=.05/3;power=.80
    n=((nd.inv_cdf(1-alpha/2)*sqrt(q)+nd.inv_cdf(power)*sqrt(q-delta**2))**2)/(delta**2)
    return {'original_confirmatory_pairs':n,'original_threshold':260,
       'precision_half_width':.10,'precision_independent_pairs':ceil(nd.inv_cdf(.975)**2*q/.10**2),
       'executed_final_condition_exception_families':4,
       'formula':'[z(1-alpha/2)*sqrt(q) + z(power)*sqrt(q-delta^2)]^2/delta^2',
       'simulations':[simulate(n,q) for n in (4,10,97,260) for q in (.10,.25,.40)],
       'claims':'Exploração descritiva. Nem poder nem alvo de precisão atingidos pela amostra final.'}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('output');a=p.parse_args();write(a.output,report())
