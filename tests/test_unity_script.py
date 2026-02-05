import numpy as np
import pytest

from unity_script import (
    TheOne,
    QuantumParticle,
    Consciousness,
    UniversalSymphony,
    generate_fractal_universe,
)


def test_quantum_particle_observe_returns_binary():
    np.random.seed(42)
    particle = QuantumParticle(2.0)
    value = particle.observe()
    assert value in (0.0, 1.0)
    assert particle.is_observed is True


def test_quantum_particle_wave_amplitude_changes_after_observe():
    np.random.seed(0)
    particle = QuantumParticle(1.0)
    t = np.linspace(0, 1, 1000)
    pre = particle.get_wave(t)
    particle.observe()
    post = particle.get_wave(t)
    assert np.max(np.abs(post)) > np.max(np.abs(pre))


def test_generate_fractal_universe_count():
    particles = generate_fractal_universe(base_freq=1.0, octaves=6)
    # Full binary tree node count: 2^(n+1) - 1
    expected = 2 ** (6 + 1) - 1
    assert len(particles) == expected


def test_universal_symphony_render_sum():
    t = np.linspace(0, 1, 100)
    p1 = QuantumParticle(1.0)
    p2 = QuantumParticle(2.0)
    p1.observe()
    p2.observe()

    universe = UniversalSymphony()
    universe.add(p1)
    universe.add(p2)

    summed = universe.render_reality(t)
    direct = p1.get_wave(t) + p2.get_wave(t)
    assert np.allclose(summed, direct)


def test_harmonic_resonance_detection():
    universe = UniversalSymphony()
    p1 = QuantumParticle(1.0)
    p2 = QuantumParticle(2.0)
    p3 = QuantumParticle(2.5)
    for p in (p1, p2, p3):
        p.observe()
        universe.add(p)

    harmonics = universe.check_harmonic_resonance(tolerance=0.01)
    freqs = sorted([p.freq for p in harmonics])
    assert freqs == [1.0, 2.0]


def test_consciousness_tune_to_source_converges():
    observer = Consciousness(frequency=7.83)
    observer.tune_to_source(target_freq=1.0, verbose=False, sleep_time=0)
    assert observer.is_aware is True
    assert observer.freq == 1.0


def test_observation_distribution_is_balanced():
    np.random.seed(123)
    trials = 1000
    observed = 0

    for _ in range(trials):
        p = QuantumParticle(1.0)
        observed += p.observe()

    ratio = observed / trials
    assert 0.4 <= ratio <= 0.6


def test_entanglement_collapses_to_same_value():
    np.random.seed(7)
    p1 = QuantumParticle(1.0)
    p2 = QuantumParticle(2.0)
    p1.entangle_with(p2)

    v1 = p1.observe()
    v2 = p2.observe()
    assert v1 == v2
    assert p1.is_observed is True
    assert p2.is_observed is True


def test_decoherence_collapses_after_time():
    np.random.seed(11)
    p = QuantumParticle(1.0, decoherence_time=0.5)
    created = p._created_at

    assert p.maybe_decohere(now=created + 0.25) is False
    assert p.is_observed is False

    assert p.maybe_decohere(now=created + 0.5) is True
    assert p.is_observed is True


def test_decoherence_reduces_coherence():
    universe = UniversalSymphony()
    particles = [QuantumParticle(1.0) for _ in range(50)]
    for p in particles:
        p.phase = 0.0
    universe.add_all(particles)

    coherence_before = universe.get_coherence()
    rng = np.random.default_rng(0)
    universe.apply_decoherence(entropy_factor=0.1, rng=rng)
    coherence_after = universe.get_coherence()

    assert coherence_before == 1.0
    assert coherence_after < coherence_before


def test_observe_all_probability():
    universe = UniversalSymphony()
    particles = [QuantumParticle(1.0) for _ in range(20)]
    universe.add_all(particles)

    observed = universe.observe_all(probability=1.0)
    assert observed == len(particles)
    assert universe.get_observed_count() == len(particles)


def test_resonance_convergence_loop_adjusts_frequency():
    universe = UniversalSymphony()
    particles = [QuantumParticle(1.0) for _ in range(30)]
    for p in particles:
        p.phase = 0.0
    universe.add_all(particles)
    
    # Introduce decoherence to create dissonance
    rng = np.random.default_rng(42)
    universe.apply_decoherence(entropy_factor=0.3, rng=rng)

    observer = Consciousness(frequency=7.83)
    observer.learning_rate = 0.5
    start_freq = observer.freq
    history = observer.resonance_convergence_loop(universe, steps=10, target_freq=1.0)

    assert len(history) == 10
    assert observer.freq < start_freq  # Frequency should decrease toward 1.0


def test_omega_time_advances():
    universe = UniversalSymphony()
    particles = [QuantumParticle(1.0), QuantumParticle(2.0)]
    universe.add_all(particles)

    before = universe.get_omega_time()
    universe.tick(dt=0.5)
    after = universe.get_omega_time()

    assert after > before
