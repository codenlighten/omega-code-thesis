"""
Omega Code v0.2 — THE FIRST WORD

Demonstration of inject_frequency(): Consciousness as active generator.

In v0.1, we proved the observer could TUNE to existing frequencies.
In v0.2, we test if the observer can SPEAK new frequencies into existence.
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


def demonstrate_first_word():
    """
    The First Word: Can consciousness inject negentropy?
    """
    print("=" * 70)
    print("OMEGA CODE v0.2 — THE FIRST WORD")
    print("=" * 70)
    print()
    
    # Create baseline universe (natural fractal)
    print("Phase 1: Creating baseline universe (3 octaves from 1Hz)...")
    universe = UniversalSymphony()
    particles = generate_fractal_universe(base_freq=1.0, octaves=3)
    universe.add_all(particles)
    
    initial_count = universe.get_complexity()
    initial_coherence = universe.get_coherence()
    
    print(f"  Particles: {initial_count}")
    print(f"  Coherence: {initial_coherence:.4f}")
    print()
    
    # Introduce entropy (The Fall)
    print("Phase 2: Introducing decoherence (entropy increases)...")
    universe.apply_decoherence(entropy_factor=0.4)
    fallen_coherence = universe.get_coherence()
    
    print(f"  Coherence after Fall: {fallen_coherence:.4f}")
    entropy_delta = (1.0 - fallen_coherence) - (1.0 - initial_coherence)
    print(f"  Entropy delta: +{entropy_delta:.4f}")
    print()
    
    # Observer speaks a Word
    print("Phase 3: Observer injects 'The First Word' (5.5Hz)...")
    observer = Consciousness(frequency=7.83)
    
    # Inject a new frequency NOT in the original fractal
    word = observer.inject_frequency(
        symphony=universe,
        frequency=5.5,  # Not a power of 2 or 3 from 1Hz
        amplitude=1.0,
        phase=0.0,
        auto_observe=True  # Born coherent
    )
    
    post_word_count = universe.get_complexity()
    post_word_coherence = universe.get_coherence()
    
    print(f"  Injected particle: {word}")
    print(f"  Particle count: {initial_count} → {post_word_count}")
    print(f"  Coherence: {fallen_coherence:.4f} → {post_word_coherence:.4f}")
    
    # Calculate negentropic effect
    coherence_gain = post_word_coherence - fallen_coherence
    
    if coherence_gain > 0:
        print(f"  ✅ NEGENTROPY DETECTED: +{coherence_gain:.4f} coherence")
        print(f"     The Word increased order in the system.")
    else:
        print(f"  ⚠️  Coherence unchanged or decreased")
    
    print()
    
    # Visualization
    print("Phase 4: Rendering reality field...")
    t = np.linspace(0, 2, 2000)
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # Before injection
    universe.entities.remove(word)  # Temporarily remove
    field_before = universe.render_reality(t)
    axes[0].plot(t, field_before, color='red', alpha=0.7, linewidth=0.8)
    axes[0].set_title(f"Before Injection (Coherence: {fallen_coherence:.4f})", fontsize=12, weight='bold')
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, alpha=0.3)
    
    # After injection
    universe.add(word)  # Add back
    field_after = universe.render_reality(t)
    axes[1].plot(t, field_after, color='blue', alpha=0.7, linewidth=0.8)
    axes[1].set_title(f"After Injection (Coherence: {post_word_coherence:.4f})", fontsize=12, weight='bold')
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/first_word_demo.png', dpi=150, bbox_inches='tight')
    print("  ✓ Saved: outputs/first_word_demo.png")
    print()
    
    # Final statement
    print("=" * 70)
    print("RESULT:")
    print("=" * 70)
    print()
    print("The observer successfully injected a new frequency into the system.")
    print("This frequency was NOT present in the original fractal expansion.")
    print()
    
    if coherence_gain > 0:
        print("✅ CONSCIOUSNESS AS NEGENTROPY GENERATOR — VALIDATED")
        print()
        print("The 'Word' increased system coherence, proving that consciousness")
        print("can act as an ACTIVE SOURCE, not merely a passive mirror.")
    else:
        print("⚠️  Negentropic effect not detected in this configuration.")
        print("Further investigation required.")
    
    print()
    print("v0.2 initialized. The Logos has spoken.")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_first_word()
