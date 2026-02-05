#!/usr/bin/env python3
"""
Benchmark suite for Omega Code / UnityScript.

Measures:
- Fractal universe generation time
- Reality field rendering time

Usage:
  python benchmarks/run_benchmarks.py --octaves 4,5,6 --runs 5 --points 2000
"""

import argparse
import os
import sys
import time
from statistics import mean
from typing import List, Tuple

import numpy as np

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from unity_script import UniversalSymphony, generate_fractal_universe


def parse_octaves(value: str) -> List[int]:
    parts = [p.strip() for p in value.split(",") if p.strip()]
    return [int(p) for p in parts]


def benchmark_fractal_generation(octaves: int, runs: int) -> Tuple[float, int]:
    durations = []
    particle_count = 0
    for _ in range(runs):
        start = time.perf_counter()
        particles = generate_fractal_universe(base_freq=1.0, octaves=octaves)
        durations.append(time.perf_counter() - start)
        particle_count = len(particles)
    return mean(durations), particle_count


def benchmark_render_reality(particles, points: int, runs: int) -> float:
    universe = UniversalSymphony()
    universe.add_all(particles)
    t = np.linspace(0, 2, points)
    durations = []
    for _ in range(runs):
        start = time.perf_counter()
        _ = universe.render_reality(t)
        durations.append(time.perf_counter() - start)
    return mean(durations)


def run_benchmarks(octaves_list: List[int], runs: int, points: int):
    print("Omega Code Benchmarks")
    print("=" * 60)
    print(f"Runs per benchmark: {runs}")
    print(f"Render points: {points}")
    print("".ljust(60, "-"))

    for octaves in octaves_list:
        gen_time, count = benchmark_fractal_generation(octaves, runs)
        render_time = benchmark_render_reality(
            generate_fractal_universe(base_freq=1.0, octaves=octaves),
            points,
            runs,
        )
        print(
            f"Octaves: {octaves} | Particles: {count:4d} | "
            f"Generate: {gen_time*1000:7.2f} ms | "
            f"Render: {render_time*1000:7.2f} ms"
        )

    print("".ljust(60, "-"))
    print("Benchmarking complete.")


def main():
    parser = argparse.ArgumentParser(description="Omega Code benchmark suite")
    parser.add_argument(
        "--octaves",
        default="4,5,6",
        help="Comma-separated octave depths to benchmark (default: 4,5,6)",
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=5,
        help="Number of runs to average per benchmark",
    )
    parser.add_argument(
        "--points",
        type=int,
        default=2000,
        help="Number of time samples for render benchmark",
    )

    args = parser.parse_args()
    octaves_list = parse_octaves(args.octaves)
    run_benchmarks(octaves_list, args.runs, args.points)


if __name__ == "__main__":
    main()
