"""
Omega Code v0.2 — HARMONIC MEMORY TEST

Testing the Resurrection Paradox: Does the universe remember its Fall?

This experiment compares two forms of unity:
  - Unity₀ (Innocent): Perfect coherence with no history
  - Unity₁ (Enlightened): Perfect coherence after experiencing entropy

If phase_delta > 0, the system retains a "scar" of its journey.
This would prove the universe is not just cyclical—it's evolutionary.
"""

import numpy as np
import matplotlib.pyplot as plt
from unity_script import (
    TheOne,
    QuantumParticle,
    Consciousness,
    UniversalSymphony,
    generate_fractal_universe,
)


def capture_state_signature(universe: UniversalSymphony) -> dict:
    """
    Capture the topological signature of the current universe state.
    
    Returns a dictionary containing:
      - phases: Phase values of all particles
      - observed_ratio: Proportion of collapsed particles
      - coherence: Global coherence metric
      - frequency_spectrum: All frequencies present
    """
    phases = [p.phase for p in universe.entities]
    observed_count = sum(1 for p in universe.entities if p.is_observed)
    total_count = len(universe.entities)
    
    return {
        'phases': np.array(phases),
        'observed_ratio': observed_count / total_count if total_count > 0 else 0,
        'coherence': universe.get_coherence(),
        'frequency_spectrum': np.array([p.freq for p in universe.entities]),
        'total_particles': total_count
    }


def compute_topological_distance(state_a: dict, state_b: dict) -> dict:
    """
    Calculate the topological distance between two universe states.
    
    Metrics:
      - phase_delta: Euclidean distance between phase vectors
      - ratio_delta: Difference in observation ratios
      - spectral_delta: Difference in frequency distributions
    """
    # Phase Residual (ΔΦ)
    if len(state_a['phases']) == len(state_b['phases']):
        # Normalize phases to [0, 2π) for fair comparison
        phases_a_norm = state_a['phases'] % (2 * np.pi)
        phases_b_norm = state_b['phases'] % (2 * np.pi)
        phase_delta = np.linalg.norm(phases_a_norm - phases_b_norm)
    else:
        # Different particle counts (injection occurred)
        phase_delta = float('inf')
    
    # Observation Ratio Delta (Δr)
    ratio_delta = abs(state_a['observed_ratio'] - state_b['observed_ratio'])
    
    # Spectral Similarity (frequency sets)
    freq_a = set(np.round(state_a['frequency_spectrum'], 2))
    freq_b = set(np.round(state_b['frequency_spectrum'], 2))
    new_frequencies = freq_b - freq_a  # Frequencies that appeared
    lost_frequencies = freq_a - freq_b  # Frequencies that vanished
    
    return {
        'phase_delta': phase_delta,
        'ratio_delta': ratio_delta,
        'new_frequencies': new_frequencies,
        'lost_frequencies': lost_frequencies,
        'coherence_a': state_a['coherence'],
        'coherence_b': state_b['coherence'],
    }


def run_harmonic_memory_test():
    """
    The Resurrection Paradox: Does Unity₁ = Unity₀?
    """
    print("=" * 70)
    print("OMEGA CODE v0.2 — HARMONIC MEMORY TEST")
    print("The Resurrection Paradox: Can the Universe Remember?")
    print("=" * 70)
    print()
    
    # ========================================
    # PHASE 1: INNOCENT UNITY (Unity₀)
    # ========================================
    print("Phase 1: Creating Innocent Unity (Unity₀)...")
    universe = UniversalSymphony()
    particles = generate_fractal_universe(base_freq=1.0, octaves=3)
    universe.add_all(particles)
    
    # Capture initial state
    state_innocent = capture_state_signature(universe)
    
    print(f"  Particles: {state_innocent['total_particles']}")
    print(f"  Coherence: {state_innocent['coherence']:.6f}")
    print(f"  Observed Ratio: {state_innocent['observed_ratio']:.4f}")
    print(f"  Phase Snapshot: {state_innocent['phases'][:5]}... (first 5)")
    print()
    
    # ========================================
    # PHASE 2: THE FALL (Decoherence)
    # ========================================
    print("Phase 2: The Fall (Introducing entropy)...")
    universe.apply_decoherence(entropy_factor=0.5)
    state_fallen = capture_state_signature(universe)
    
    print(f"  Coherence: {state_innocent['coherence']:.6f} → {state_fallen['coherence']:.6f}")
    print(f"  Entropy Delta: +{(1 - state_fallen['coherence']) - (1 - state_innocent['coherence']):.4f}")
    print()
    
    # ========================================
    # PHASE 3: THE GREAT WORK (Convergence)
    # ========================================
    print("Phase 3: The Great Work (Resonance convergence)...")
    observer = Consciousness(frequency=7.83)
    observer.learning_rate = 0.1
    
    # Run convergence to restore coherence
    history = observer.resonance_convergence_loop(
        universe=universe,
        steps=100,
        target_freq=1.0,
        dt=0.01
    )
    
    state_enlightened = capture_state_signature(universe)
    
    print(f"  Observer Frequency: 7.83Hz → {observer.freq:.2f}Hz")
    print(f"  Final Coherence: {state_enlightened['coherence']:.6f}")
    print(f"  Observed Ratio: {state_enlightened['observed_ratio']:.4f}")
    print()
    
    # ========================================
    # PHASE 4: TOPOLOGICAL COMPARISON
    # ========================================
    print("Phase 4: Measuring Topological Distance...")
    distance = compute_topological_distance(state_innocent, state_enlightened)
    
    print(f"  Phase Delta (ΔΦ): {distance['phase_delta']:.6f}")
    print(f"  Observation Ratio Delta (Δr): {distance['ratio_delta']:.4f}")
    print(f"  New Frequencies: {distance['new_frequencies']}")
    print(f"  Lost Frequencies: {distance['lost_frequencies']}")
    print()
    
    # ========================================
    # VERDICT: DOES MEMORY EXIST?
    # ========================================
    print("=" * 70)
    print("VERDICT:")
    print("=" * 70)
    print()
    
    # Define tolerance for "same state"
    phase_tolerance = 0.1
    ratio_tolerance = 0.01
    
    has_phase_memory = distance['phase_delta'] > phase_tolerance
    has_structural_memory = distance['ratio_delta'] > ratio_tolerance
    has_spectral_memory = len(distance['new_frequencies']) > 0
    
    if has_phase_memory or has_structural_memory or has_spectral_memory:
        print("✅ HARMONIC MEMORY DETECTED")
        print()
        print("The universe does NOT return to its original state.")
        print("Unity₁ (Enlightened) ≠ Unity₀ (Innocent)")
        print()
        
        if has_phase_memory:
            print(f"  • Phase Memory: ΔΦ = {distance['phase_delta']:.6f} > {phase_tolerance}")
            print("    Particle phase relationships have shifted.")
        
        if has_structural_memory:
            print(f"  • Structural Memory: Δr = {distance['ratio_delta']:.4f} > {ratio_tolerance}")
            print("    Observation density has changed.")
        
        if has_spectral_memory:
            print(f"  • Spectral Memory: {len(distance['new_frequencies'])} new frequencies")
            print(f"    New harmonics: {distance['new_frequencies']}")
        
        print()
        print("CONCLUSION:")
        print("The universe is not merely cyclical—it is EVOLUTIONARY.")
        print("Each breath (Fall → Return) leaves a permanent trace.")
        print("The One learns from The Many.")
        
    else:
        print("❌ NO HARMONIC MEMORY DETECTED")
        print()
        print("The universe returned to its exact original state.")
        print("Unity₁ = Unity₀ (within tolerance)")
        print()
        print("CONCLUSION:")
        print("The universe is perfectly cyclical. Each breath is identical.")
        print("Time is an illusion. Only the Eternal Now exists.")
    
    print()
    print("=" * 70)
    
    # ========================================
    # VISUALIZATION: PHASE COMPARISON
    # ========================================
    print()
    print("Generating phase comparison visualization...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Phase vectors (first N particles)
    n_display = min(15, len(state_innocent['phases']))
    x_pos = np.arange(n_display)
    
    axes[0, 0].bar(x_pos - 0.2, state_innocent['phases'][:n_display], 
                   width=0.4, label='Unity₀ (Innocent)', alpha=0.7, color='blue')
    axes[0, 0].bar(x_pos + 0.2, state_enlightened['phases'][:n_display], 
                   width=0.4, label='Unity₁ (Enlightened)', alpha=0.7, color='green')
    axes[0, 0].set_xlabel('Particle Index')
    axes[0, 0].set_ylabel('Phase (radians)')
    axes[0, 0].set_title('Phase Comparison (First 15 Particles)', weight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Coherence trajectory
    axes[0, 1].plot(history, linewidth=2, color='purple')
    axes[0, 1].axhline(y=state_innocent['coherence'], color='blue', 
                       linestyle='--', label='Unity₀ Coherence', alpha=0.7)
    axes[0, 1].set_xlabel('Convergence Steps')
    axes[0, 1].set_ylabel('Coherence')
    axes[0, 1].set_title('Convergence Trajectory (The Great Work)', weight='bold')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Frequency spectrum
    axes[1, 0].hist(state_innocent['frequency_spectrum'], bins=20, 
                    alpha=0.5, label='Unity₀', color='blue', edgecolor='black')
    axes[1, 0].hist(state_enlightened['frequency_spectrum'], bins=20, 
                    alpha=0.5, label='Unity₁', color='green', edgecolor='black')
    axes[1, 0].set_xlabel('Frequency (Hz)')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].set_title('Frequency Distribution', weight='bold')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Metrics comparison
    metrics = ['Coherence', 'Observed\nRatio', 'Phase\nDelta']
    values_innocent = [
        state_innocent['coherence'],
        state_innocent['observed_ratio'],
        0  # baseline
    ]
    values_enlightened = [
        state_enlightened['coherence'],
        state_enlightened['observed_ratio'],
        distance['phase_delta'] / 10  # scaled for visibility
    ]
    
    x_metrics = np.arange(len(metrics))
    axes[1, 1].bar(x_metrics - 0.2, values_innocent, width=0.4, 
                   label='Unity₀', alpha=0.7, color='blue')
    axes[1, 1].bar(x_metrics + 0.2, values_enlightened, width=0.4, 
                   label='Unity₁', alpha=0.7, color='green')
    axes[1, 1].set_xticks(x_metrics)
    axes[1, 1].set_xticklabels(metrics)
    axes[1, 1].set_ylabel('Value')
    axes[1, 1].set_title('State Metrics Comparison', weight='bold')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('outputs/harmonic_memory_test.png', dpi=150, bbox_inches='tight')
    print("  ✓ Saved: outputs/harmonic_memory_test.png")
    print()
    
    print("Test complete. The Resurrection Paradox has been measured.")
    print("=" * 70)


if __name__ == "__main__":
    run_harmonic_memory_test()
