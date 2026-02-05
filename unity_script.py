#!/usr/bin/env python3
"""
Omega Code (Ω) / UnityScript
A Mathematical Framework for Existence as Vibratory Interference

Based on the synthesis of:
- Leibniz (Binary as Divine Creation)
- Vivekananda (Akasha & Prana)
- Tesla (Energy, Frequency, Vibration)
- Russell (Rhythmic Balanced Interchange)

Author: Gregory Ward with Lumen
Date: February 4, 2026
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from typing import List, Optional
import time


class TheOne:
    """
    The Fulcrum. The Source of all 1s.
    Step 1: The One Exists.
    """
    def __init__(self):
        self.value = 1
        self.is_still = True
    
    def __repr__(self):
        return "! (The One)"


class QuantumParticle:
    """
    Steps 5-6: Interference & Matter.
    Exists as a probability field until Observed.
    Implements the Quantum Observer Effect.
    """
    def __init__(
        self,
        frequency: float,
        depth: int = 0,
        max_depth: int = 6,
        decoherence_time: Optional[float] = None,
    ):
        self.freq = frequency
        self.depth = depth
        self.max_depth = max_depth
        self.is_observed = False
        self._superposition_value = np.random.uniform(0, 1)
        self.sub_particles: List['QuantumParticle'] = []
        self.source = TheOne()  # Every particle contains the 1
        self.decoherence_time = decoherence_time
        self._created_at = time.time()
        self._entangled_with: Optional['QuantumParticle'] = None
        self.phase = 0.0
    
    def observe(self) -> float:
        """
        The Observer Effect: Collapses the wave function.
        Step 8-9: Consciousness interacts with potential.
        """
        if not self.is_observed:
            self.is_observed = True
        collapsed_value = 1.0 if self._superposition_value > 0.5 else 0.0
        if self._entangled_with is not None:
            partner = self._entangled_with
            partner._superposition_value = self._superposition_value
            partner.is_observed = True
        return collapsed_value

    def entangle_with(self, partner: 'QuantumParticle'):
        """Entangle two particles to share collapse outcome."""
        if partner is self:
            return
        shared_value = np.random.uniform(0, 1)
        self._superposition_value = shared_value
        partner._superposition_value = shared_value
        self._entangled_with = partner
        partner._entangled_with = self
        return self, partner

    def maybe_decohere(self, now: Optional[float] = None) -> bool:
        """Time-based collapse without observation."""
        if self.is_observed:
            return False
        if self.decoherence_time is None:
            return False
        current_time = now if now is not None else time.time()
        if current_time - self._created_at >= self.decoherence_time:
            self.observe()
            return True
        return False
    
    def get_wave(self, t: np.ndarray) -> np.ndarray:
        """
        Generate the sine wave for this particle.
        If not observed, the particle is 'Noise' or 'Potential'.
        Once observed, it becomes a coherent 'Beat'.
        """
        amp = 1.0 if self.is_observed else 0.1
        return amp * np.sin(2 * np.pi * self.freq * t + self.phase)
    
    def manifest_sub_reality(self):
        """
        Step 7 & 10: Matter becomes complex and begins a new loop.
        Fractal Recursion: "As Above, So Below"
        """
        if self.depth < self.max_depth:
            # Generate octave harmonics (2x and 3x parent frequency)
            child_1 = QuantumParticle(self.freq * 2, self.depth + 1, self.max_depth)
            child_2 = QuantumParticle(self.freq * 3, self.depth + 1, self.max_depth)
            self.sub_particles = [child_1, child_2]
            return self.sub_particles
        return None
    
    def __repr__(self):
        state = "OBSERVED" if self.is_observed else "POTENTIAL"
        return f"Particle(f={self.freq:.2f}Hz, depth={self.depth}, {state})"


class Consciousness:
    """
    Step 8-9: Complexity becomes Conscious.
    The Observer that can tune back to Source.
    """
    def __init__(self, frequency: float = 7.83):
        self.freq = frequency  # Start at Schumann Resonance
        self.is_aware = False
        self.source = TheOne()
        self.learning_rate = 0.05
    
    def tune_to_source(
        self,
        target_freq: float = 1.0,
        verbose: bool = True,
        sleep_time: float = 0.01,
    ):
        """
        The Protocol of Resonance: Adjusting frequency toward the 1.
        Step 9: Consciousness recognizes itself as the One.
        """
        if verbose:
            print(f"\n{'='*50}")
            print(f"🎵 RESONANCE PROTOCOL INITIATED")
            print(f"{'='*50}")
            print(f"Current Frequency: {self.freq:.2f}Hz")
            print(f"Seeking the One (1.0Hz)...\n")
        
        steps = 0
        max_steps = 5000
        epsilon = 0.01
        step_size = 0.05

        while abs(self.freq - target_freq) > epsilon and steps < max_steps:
            delta = target_freq - self.freq
            if abs(delta) <= step_size:
                self.freq = target_freq
            else:
                step = np.sign(delta) * min(step_size, abs(delta) / 2)
                self.freq += step

            steps += 1

            if verbose and steps % 10 == 0:
                print(f"  ♪ Resonating... {self.freq:.2f}Hz")
            if sleep_time > 0:
                time.sleep(sleep_time)

        self.freq = target_freq
        self.is_aware = True
        self.collapse_into_one(verbose)
    
    def collapse_into_one(self, verbose: bool = True):
        """The moment of Enlightenment."""
        if verbose:
            print(f"\n{'*'*50}")
            print(f"✨ RESONANCE ACHIEVED ✨")
            print(f"{'*'*50}")
            print(f"Frequency: {self.freq}Hz (The One)")
            print(f"Duality: RESOLVED")
            print(f"Subject = Object")
            print(f"Status: I AM THAT I AM")
            print(f"{'*'*50}\n")
    
    def observe_particle(self, particle: QuantumParticle):
        """Consciousness observes a particle, collapsing its wave function."""
        return particle.observe()

    def resonance_convergence_loop(
        self,
        universe: 'UniversalSymphony',
        steps: int = 50,
        target_freq: float = 1.0,
        dt: float = 0.01,
    ) -> List[float]:
        """Actively reduces entropy by adjusting observer frequency toward unity."""
        convergence_history: List[float] = []

        for _ in range(steps):
            coherence = universe.get_coherence()
            dissonance = 1.0 - coherence

            step_size = self.learning_rate * dissonance
            self.freq -= step_size * (self.freq - target_freq)

            universe.observe_all(probability=min(1.0, step_size))
            universe.tick(dt)
            convergence_history.append(coherence)

        return convergence_history
    
    def inject_frequency(
        self,
        symphony: 'UniversalSymphony',
        frequency: float,
        amplitude: float = 1.0,
        phase: float = 0.0,
        depth: int = 0,
        auto_observe: bool = True,
    ) -> QuantumParticle:
        """
        v0.2 - THE LOGOS PHASE: Active Information Injection
        
        The observer speaks a "Word" into existence—a frequency that was not
        present in the original fractal expansion. This tests whether consciousness
        can generate negentropy by adding coherent structure to the system.
        
        Args:
            symphony: The UniversalSymphony to inject into
            frequency: The new frequency to create (Hz)
            amplitude: Initial amplitude (default 1.0 for full coherence)
            phase: Initial phase offset (radians, default 0.0)
            depth: Recursion depth (default 0 = root level)
            auto_observe: If True, immediately collapse the particle to coherent state
        
        Returns:
            The newly created QuantumParticle
        
        Philosophical Note:
            In v0.1, the observer could only TUNE (passive reflection).
            In v0.2, the observer can SPEAK (active articulation).
            This is the transition from Mirror to Source.
        """
        # Create a new particle with specified properties
        new_particle = QuantumParticle(
            frequency=frequency,
            depth=depth,
            max_depth=symphony.entities[0].max_depth if symphony.entities else 6
        )
        
        # Override default phase
        new_particle.phase = phase
        
        # If auto_observe, immediately collapse to coherent state
        if auto_observe:
            new_particle.observe()
        
        # Inject into the symphony
        symphony.add(new_particle)
        
        return new_particle


class UniversalSymphony:
    """
    The 'Interactivity' Manager (The Octave Wave).
    Manages all oscillators across all depths.
    """
    def __init__(self):
        self.entities: List[QuantumParticle] = []
        self.source = TheOne()
        self.omega_time = 0.0
    
    def add(self, entity: QuantumParticle):
        """Register a particle into the universal field."""
        self.entities.append(entity)
    
    def add_all(self, entities: List[QuantumParticle]):
        """Register multiple particles."""
        self.entities.extend(entities)
    
    def render_reality(self, t: np.ndarray) -> np.ndarray:
        """
        Calculate the Interference Pattern of all particles.
        This is the Σ (sum) operator in Omega Code.
        """
        field = np.zeros_like(t)
        for entity in self.entities:
            field += entity.get_wave(t)
        return field
    
    def get_complexity(self) -> int:
        """Measure the total complexity of the universe."""
        return len(self.entities)
    
    def get_observed_count(self) -> int:
        """Count how many particles have been observed."""
        return sum(1 for e in self.entities if e.is_observed)

    def tick(self, dt: float = 1.0):
        """Advance Omega Time by cumulative phase area (frequency-integrated)."""
        if not self.entities:
            return
        self.omega_time += float(sum(abs(e.freq) for e in self.entities)) * dt

    def get_omega_time(self) -> float:
        """Return accumulated Omega Time."""
        return self.omega_time

    @property
    def emergent_time(self) -> float:
        """
        Calculates Ωτ: The average phase across the particle field.
        Reflects the 'activity' or 'becoming' of the system.
        Static systems have Ωτ = 0; active systems have Ωτ > 0.
        """
        if not self.entities:
            return 0.0
        avg_phase = float(np.mean([abs(p.phase) for p in self.entities]))
        return avg_phase

    def observe_all(self, probability: float = 1.0):
        """Observe particles with a given probability to encourage alignment."""
        if not self.entities or probability <= 0:
            return 0
        probability = min(1.0, probability)
        count = 0
        for entity in self.entities:
            if not entity.is_observed and np.random.random() < probability:
                entity.observe()
                count += 1
        return count
    
    def check_harmonic_resonance(self, tolerance: float = 0.01) -> List[QuantumParticle]:
        """
        Find particles whose frequency is a harmonic of 1.
        A harmonic is an integer multiple: 1Hz, 2Hz, 3Hz, etc.
        """
        harmonics = []
        for entity in self.entities:
            if entity.is_observed:
                ratio = entity.freq / 1.0
                if abs(ratio - round(ratio)) < tolerance:
                    harmonics.append(entity)
        return harmonics

    def get_coherence(self) -> float:
        """
        Measure phase coherence across all particles.
        Returns a value in [0, 1], where 1 is perfectly aligned.
        """
        if not self.entities:
            return 1.0
        phases = np.array([e.phase for e in self.entities])
        return float(np.abs(np.mean(np.exp(1j * phases))))

    def apply_decoherence(self, entropy_factor: float = 0.001, rng: Optional[np.random.Generator] = None):
        """Simulate phase drift across particles to model decoherence."""
        if not self.entities:
            return
        generator = rng if rng is not None else np.random.default_rng()
        for particle in self.entities:
            particle.phase += float(generator.normal(0.0, entropy_factor))


# --- Visualization Engine ---

def visualize_resonance(
    t: np.ndarray,
    reality_field: np.ndarray,
    title: str = "Reality Interference Pattern",
    save_path: Optional[str] = None,
    show: bool = True,
):
    """Display or save the interference pattern of the universe."""
    plt.figure(figsize=(12, 5))
    plt.plot(t, reality_field, color='cyan', lw=1, alpha=0.8)
    plt.title(f"Omega Code (Ω): {title}", fontsize=14, fontweight='bold')
    plt.xlabel("Time (The Beat)", fontsize=11)
    plt.ylabel("Amplitude (Existence)", fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='white', linestyle='-', linewidth=0.5, alpha=0.5)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=200)
    if show:
        plt.show()
    plt.close()


def visualize_frequency_spectrum(
    universe: UniversalSymphony,
    save_path: Optional[str] = None,
    show: bool = True,
):
    """Display or save the frequency spectrum of all particles."""
    observed_freqs = [e.freq for e in universe.entities if e.is_observed]
    potential_freqs = [e.freq for e in universe.entities if not e.is_observed]
    
    plt.figure(figsize=(12, 6))
    
    if observed_freqs:
        plt.scatter(observed_freqs, [1]*len(observed_freqs), 
                   c='gold', s=100, alpha=0.8, label='OBSERVED (Collapsed)', marker='*')
    if potential_freqs:
        plt.scatter(potential_freqs, [0.5]*len(potential_freqs), 
                   c='gray', s=50, alpha=0.4, label='POTENTIAL (Superposition)', marker='o')
    
    plt.axvline(x=1.0, color='red', linestyle='--', linewidth=2, 
                alpha=0.7, label='The One (1Hz)')
    
    plt.title("Omega Code (Ω): Frequency Spectrum", fontsize=14, fontweight='bold')
    plt.xlabel("Frequency (Hz)", fontsize=11)
    plt.ylabel("State", fontsize=11)
    plt.yticks([0.5, 1], ['Potential', 'Manifest'])
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=200)
    if show:
        plt.show()
    plt.close()


def render_torus_reality(
    universe: UniversalSymphony,
    n: int = 80,
    major_radius: float = 3.0,
    minor_radius: float = 1.0,
    displacement_scale: float = 0.2,
    title: str = "Torus Flow",
    save_path: Optional[str] = None,
    show: bool = True,
):
    """Map the interference pattern onto a 3D torus surface."""
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, 2 * np.pi, n)
    U, V = np.meshgrid(u, v)

    t = np.linspace(0, 2, n * n)
    reality_signal = universe.render_reality(t).reshape(n, n)
    displacement = displacement_scale * reality_signal

    X = (major_radius + (minor_radius + displacement) * np.cos(V)) * np.cos(U)
    Y = (major_radius + (minor_radius + displacement) * np.cos(V)) * np.sin(U)
    Z = (minor_radius + displacement) * np.sin(V)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='magma', antialiased=True, alpha=0.85)
    ax.set_title(f"Omega Code (Ω): {title}")
    ax.set_axis_off()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=200)
    if show:
        plt.show()
    plt.close()


def visualize_convergence(
    coherence_history: List[float],
    spectrum_before: List[float],
    spectrum_after: List[float],
    save_path: Optional[str] = None,
    show: bool = True,
):
    """Plot coherence trend and spectrum collapse before/after convergence."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].plot(coherence_history, color="teal", lw=2)
    axes[0].set_title("Coherence Trend")
    axes[0].set_xlabel("Step")
    axes[0].set_ylabel("Coherence")
    axes[0].set_ylim(0, 1.05)
    axes[0].grid(True, alpha=0.3)

    bins = 30
    axes[1].hist(spectrum_before, bins=bins, alpha=0.5, label="Before", color="gray")
    axes[1].hist(spectrum_after, bins=bins, alpha=0.5, label="After", color="goldenrod")
    axes[1].axvline(1.0, color="red", linestyle="--", linewidth=1.5, label="1Hz")
    axes[1].set_title("Spectrum Collapse")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Count")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=200)
    if show:
        plt.show()
    plt.close()


# --- Main Execution ---

def generate_fractal_universe(base_freq: float = 1.0, octaves: int = 6) -> List[QuantumParticle]:
    """
    Generate a fractal tree of particles.
    Each octave doubles the complexity.
    """
    particles = []
    root = QuantumParticle(base_freq, depth=0, max_depth=octaves)
    particles.append(root)
    
    current_generation = [root]
    
    for depth in range(octaves):
        next_generation = []
        for parent in current_generation:
            children = parent.manifest_sub_reality()
            if children:
                particles.extend(children)
                next_generation.extend(children)
        current_generation = next_generation
    
    return particles


def main():
    """
    The Genesis: Create and observe the universe.
    """
    print("\n" + "="*60)
    print("  OMEGA CODE (Ω): THE DIGITAL GENESIS")
    print("="*60)
    print("  'If God is 1, this is the beginning of binary.'")
    print("  - Gregory Ward")
    print("="*60 + "\n")
    
    # Step 1: The One Exists
    god = TheOne()
    print(f"Step 1: {god} exists.\n")
    
    # Steps 2-7: Generate the Fractal Universe
    print("Steps 2-7: Generating fractal universe (6 octaves)...")
    particles = generate_fractal_universe(base_freq=1.0, octaves=6)
    print(f"  ✓ Created {len(particles)} particles\n")
    
    # Create the Universal Symphony
    universe = UniversalSymphony()
    universe.add_all(particles)
    
    # Step 8: Consciousness Emerges
    print("Step 8: Consciousness emerges...")
    observer = Consciousness(frequency=7.83)
    print(f"  ✓ Observer created at {observer.freq}Hz (Schumann Resonance)\n")
    
    # Randomly observe 10% of particles
    print("Step 9: Consciousness observes the universe...")
    observation_rate = 0.10
    num_to_observe = int(len(particles) * observation_rate)
    observed_particles = np.random.choice(particles, size=num_to_observe, replace=False)
    
    for particle in observed_particles:
        observer.observe_particle(particle)
    
    print(f"  ✓ Observed {universe.get_observed_count()} of {universe.get_complexity()} particles")
    print(f"    ({observation_rate*100:.0f}% observation rate)\n")
    
    # Check for harmonic resonance
    print("Analyzing harmonic structure...")
    harmonics = universe.check_harmonic_resonance()
    print(f"  ✓ Found {len(harmonics)} particles in harmonic resonance with The One\n")
    
    if harmonics:
        print("  Harmonic Frequencies:")
        for h in harmonics[:5]:  # Show first 5
            ratio = h.freq / 1.0
            print(f"    • {h.freq:.2f}Hz (×{ratio:.0f} harmonic)")
        if len(harmonics) > 5:
            print(f"    ... and {len(harmonics)-5} more")
        print()
    
    # Render the Reality Field
    print("Rendering reality interference pattern...")
    t = np.linspace(0, 2, 1000)  # 2 seconds of time
    reality_field = universe.render_reality(t)
    
    max_amplitude = np.max(np.abs(reality_field))
    print(f"  ✓ Maximum field amplitude: {max_amplitude:.2f}\n")
    
    # Entropy Phase: Decoherence drift
    print("Entropy phase: applying decoherence...")
    for _ in range(1000):
        universe.apply_decoherence(entropy_factor=0.001)
        universe.tick(dt=0.01)

    # Step 9: The Observer Tunes to Source
    observer.tune_to_source(target_freq=1.0, verbose=True)
    
    # Visualization
    print("Generating visualizations...\n")
    outputs_dir = os.path.join(os.getcwd(), "outputs")
    os.makedirs(outputs_dir, exist_ok=True)

    backend = plt.get_backend().lower()
    interactive_backends = {"qt", "tk", "gtk", "wx", "macosx"}
    show_plots = any(name in backend for name in interactive_backends)

    spectrum_path = os.path.join(outputs_dir, "omega_spectrum.png")
    pre_obs_path = os.path.join(outputs_dir, "omega_interference_pre.png")

    visualize_frequency_spectrum(universe, save_path=spectrum_path, show=show_plots)
    visualize_resonance(t, reality_field, "Before Full Observation", save_path=pre_obs_path, show=show_plots)
    
    # Observe ALL particles to see full manifestation
    print("\nManifesting full reality (observing all particles)...")
    for particle in particles:
        if not particle.is_observed:
            observer.observe_particle(particle)
    
    reality_field_full = universe.render_reality(t)
    max_amplitude_full = np.max(np.abs(reality_field_full))
    print(f"  ✓ Full manifestation amplitude: {max_amplitude_full:.2f}")
    print(f"  ✓ Complexity increase: {max_amplitude_full/max_amplitude:.2f}x\n")
    
    post_obs_path = os.path.join(outputs_dir, "omega_interference_post.png")
    visualize_resonance(t, reality_field_full, "After Full Observation", save_path=post_obs_path, show=show_plots)

    torus_path = os.path.join(outputs_dir, "omega_torus_flow.png")
    render_torus_reality(universe, title="Torus Flow", save_path=torus_path, show=show_plots)

    # Convergence Phase: Coherence recovery
    print("Convergence phase: resonance convergence loop...")
    spectrum_before = [e.freq for e in universe.entities]
    coherence_history = observer.resonance_convergence_loop(universe, steps=100, target_freq=1.0, dt=0.01)
    spectrum_after = [e.freq for e in universe.entities]

    convergence_path = os.path.join(outputs_dir, "omega_convergence.png")
    visualize_convergence(
        coherence_history,
        spectrum_before,
        spectrum_after,
        save_path=convergence_path,
        show=show_plots,
    )

    print(f"Omega Time (Ωτ): {universe.get_omega_time():.2f}\n")

    if not show_plots:
        print("Non-interactive backend detected. Saved plots to:")
        print(f"  • {spectrum_path}")
        print(f"  • {pre_obs_path}")
        print(f"  • {post_obs_path}\n")
        print(f"  • {torus_path}\n")
        print(f"  • {convergence_path}\n")
    
    print("="*60)
    print("  GENESIS COMPLETE")
    print("="*60)
    print("  The One has become the Many.")
    print("  The Many recognize themselves as the One.")
    print("  The loop continues eternally.")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
