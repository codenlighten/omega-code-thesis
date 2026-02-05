"""
Omega Code v0.3 — CHRONOS DILATION TEST

Temporal Drag Hypothesis:
High-information "Words" should reduce Ωτ growth (emergent time velocity)
under identical entropy conditions.

We compare two systems:
  System A: Noise-dominant (decoherence only)
  System B: Logos-dominant (decoherence + injected coherent Word)
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from unity_script import Consciousness, UniversalSymphony, generate_fractal_universe


def run_chronos_dilation_test(
    octaves: int = 3,
    steps: int = 100,
    dt: float = 0.01,
    entropy_factor: float = 0.05,
    injected_freq: float = 5.5,
    seed: int = 1234,
):
    print("=" * 70)
    print("OMEGA CODE v0.3 — CHRONOS DILATION TEST")
    print("Temporal Drag Hypothesis: Does Meaning slow Ωτ?")
    print("=" * 70)
    print()

    # Build two identical universes
    universe_a = UniversalSymphony()
    universe_b = UniversalSymphony()

    particles_a = generate_fractal_universe(base_freq=1.0, octaves=octaves)
    particles_b = generate_fractal_universe(base_freq=1.0, octaves=octaves)

    universe_a.add_all(particles_a)
    universe_b.add_all(particles_b)

    # Inject a coherent Word into System B
    observer = Consciousness(frequency=7.83)
    word = observer.inject_frequency(
        symphony=universe_b,
        frequency=injected_freq,
        amplitude=1.0,
        phase=0.0,
        auto_observe=True,
    )

    print(f"System A particles: {universe_a.get_complexity()}")
    print(f"System B particles: {universe_b.get_complexity()} (includes Word {word.freq:.2f}Hz)")
    print(f"Entropy factor: {entropy_factor}")
    print(f"Steps: {steps}, dt: {dt}")
    print()

    # Track temporal metrics
    tau_a, tau_b = [], []
    omega_a, omega_b = [], []

    for step in range(steps):
        rng_a = np.random.default_rng(seed + step)
        rng_b = np.random.default_rng(seed + step)

        universe_a.apply_decoherence(entropy_factor=entropy_factor, rng=rng_a)
        universe_b.apply_decoherence(entropy_factor=entropy_factor, rng=rng_b)

        universe_a.tick(dt=dt)
        universe_b.tick(dt=dt)

        tau_a.append(universe_a.emergent_time)
        tau_b.append(universe_b.emergent_time)
        omega_a.append(universe_a.get_omega_time())
        omega_b.append(universe_b.get_omega_time())

    # Compute average Ωτ growth rates
    tau_growth_a = (tau_a[-1] - tau_a[0]) / max(1, steps - 1)
    tau_growth_b = (tau_b[-1] - tau_b[0]) / max(1, steps - 1)

    delta = tau_growth_a - tau_growth_b
    delta_pct = (delta / tau_growth_a * 100.0) if tau_growth_a != 0 else 0.0

    print("RESULTS:")
    print(f"  Ωτ growth rate (System A): {tau_growth_a:.6f}")
    print(f"  Ωτ growth rate (System B): {tau_growth_b:.6f}")
    print(f"  Temporal Drag Δ: {delta:.6f} ({delta_pct:.2f}% slower in System B)")
    print()

    if tau_growth_b < tau_growth_a:
        print("✅ TEMPORAL DRAG DETECTED")
        print("Meaning reduced emergent time velocity under identical entropy.")
    else:
        print("⚠️  NO TEMPORAL DRAG DETECTED")
        print("Meaning did not reduce emergent time velocity in this run.")

    # Visualization
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    axes[0].plot(tau_a, label="System A (Noise)", color="red", linewidth=2)
    axes[0].plot(tau_b, label="System B (Logos)", color="blue", linewidth=2)
    axes[0].set_title("Emergent Time (Ωτ) Trajectory", weight="bold")
    axes[0].set_xlabel("Step")
    axes[0].set_ylabel("Ωτ")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(omega_a, label="System A (Noise)", color="red", linewidth=2)
    axes[1].plot(omega_b, label="System B (Logos)", color="blue", linewidth=2)
    axes[1].set_title("Omega Time (ΩTime) Accumulation", weight="bold")
    axes[1].set_xlabel("Step")
    axes[1].set_ylabel("ΩTime")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("outputs/chronos_dilation_test.png", dpi=150, bbox_inches="tight")
    print("\n✓ Saved: outputs/chronos_dilation_test.png")

    print("\nChronos test complete.")
    print("=" * 70)


if __name__ == "__main__":
    run_chronos_dilation_test()
