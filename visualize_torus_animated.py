#!/usr/bin/env python3
"""
visualize_torus_animated.py - Animated Torus Flow Visualization

Maps the internal state of the Omega Code system to a breathing torus manifold:
  - Radial Displacement: Interference sum (total field amplitude)
  - Surface Color: Coherence metric (blue=unity, red=decoherence)
  - Rotation Speed: Emergent Time (Ωτ) velocity

Author: Gregory Ward (with Lumen)
Date: February 4, 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter
from typing import Tuple, Optional
import os


def generate_torus_coordinates(
    u: np.ndarray,
    v: np.ndarray,
    major_radius: float = 2.0,
    minor_radius: float = 1.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate standard torus surface coordinates.
    
    Parameters:
      u, v: Meshgrid angles (0 to 2π)
      major_radius: Distance from torus center to tube center
      minor_radius: Radius of the tube itself
    
    Returns:
      X, Y, Z: Surface coordinates
    """
    X = (major_radius + minor_radius * np.cos(v)) * np.cos(u)
    Y = (major_radius + minor_radius * np.cos(v)) * np.sin(u)
    Z = minor_radius * np.sin(v)
    return X, Y, Z


def apply_coherence_deformation(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    coherence: float,
    interference_amplitude: float = 1.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Deform torus surface based on coherence and interference.
    
    - Coherence = 1.0: Smooth, perfect radial harmony
    - Coherence < 1.0: Jagged, phase-shifted deformation
    - Interference amplitude modulates the degree of deformation
    
    Parameters:
      X, Y, Z: Original torus coordinates
      coherence: Phase alignment metric (0 to 1)
      interference_amplitude: Magnitude of surface displacement
    
    Returns:
      X_def, Y_def, Z_def: Deformed coordinates
    """
    # Calculate radial distance from torus center
    rho = np.sqrt(X**2 + Y**2)
    
    # Coherence inversely affects noise: high coherence = smooth, low = jagged
    noise_factor = (1.0 - coherence) * interference_amplitude
    
    # Add high-frequency deformation to the surface (phase noise)
    theta = np.arctan2(Y, X)
    phi = np.arctan2(Z, rho - 2.0)  # Angle relative to tube center
    
    deformation = noise_factor * (
        0.2 * np.sin(5 * theta) * np.cos(5 * phi) +
        0.15 * np.cos(3 * theta) * np.sin(3 * phi)
    )
    
    # Also add radial breathing based on coherence (smooth oscillation)
    breathing = 0.1 * coherence * np.sin(theta)
    
    # Scale deformation by coherence (harmony suppresses chaos)
    total_deformation = deformation * (1.0 - coherence * 0.5) + breathing
    
    # Apply deformation in radial direction
    r_tube = np.sqrt((rho - 2.0)**2 + Z**2)
    r_tube = np.maximum(r_tube, 0.01)  # Avoid division by zero
    
    X_def = X + (total_deformation * (X / (rho + 0.01)))
    Y_def = Y + (total_deformation * (Y / (rho + 0.01)))
    Z_def = Z + (total_deformation * (Z / (r_tube + 0.01)))
    
    return X_def, Y_def, Z_def


def create_torus_frame(
    coherence: float,
    interference_amplitude: float = 1.0,
    rotation_angle: float = 0.0,
    major_radius: float = 2.0,
    minor_radius: float = 1.0,
    resolution: int = 50,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Create a single torus frame with deformation based on system state.
    
    Parameters:
      coherence: Phase alignment (0 to 1)
      interference_amplitude: Magnitude of surface deformation
      rotation_angle: Rotation in degrees (for animation)
      major_radius, minor_radius: Torus geometry
      resolution: Surface grid resolution
    
    Returns:
      X_def, Y_def, Z_def: Deformed coordinates
      C: Coherence colormap values
    """
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, 2 * np.pi, resolution)
    u_mesh, v_mesh = np.meshgrid(u, v)
    
    # Generate base torus
    X, Y, Z = generate_torus_coordinates(u_mesh, v_mesh, major_radius, minor_radius)
    
    # Apply rotation for animation
    rot_rad = np.radians(rotation_angle)
    X_rot = X * np.cos(rot_rad) - Y * np.sin(rot_rad)
    Y_rot = X * np.sin(rot_rad) + Y * np.cos(rot_rad)
    
    # Apply coherence-based deformation
    X_def, Y_def, Z_def = apply_coherence_deformation(
        X_rot, Y_rot, Z,
        coherence=coherence,
        interference_amplitude=interference_amplitude,
    )
    
    # Create colormap: blue (coherent) to red (decoherent)
    C = np.full_like(X_def, coherence)
    
    return X_def, Y_def, Z_def, C


def render_torus_snapshot(
    coherence: float,
    interference_amplitude: float = 1.0,
    title: str = "Torus Flow",
    save_path: Optional[str] = None,
    rotation_angle: float = 0.0,
    cmap: str = 'RdYlBu_r',  # Red (low coherence) to Blue (high coherence)
):
    """
    Render a single torus snapshot and optionally save it.
    
    Parameters:
      coherence: Phase alignment metric
      interference_amplitude: Surface deformation magnitude
      title: Plot title
      save_path: Path to save PNG
      rotation_angle: Rotation in degrees
      cmap: Matplotlib colormap
    """
    X, Y, Z, C = create_torus_frame(
        coherence=coherence,
        interference_amplitude=interference_amplitude,
        rotation_angle=rotation_angle,
    )
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(X, Y, Z, facecolors=cm.get_cmap(cmap)(C), 
                           rstride=1, cstride=1, shade=False, alpha=0.9)
    
    ax.set_xlabel("X (Manifestation)")
    ax.set_ylabel("Y (Manifestation)")
    ax.set_zlabel("Z (Consciousness)")
    ax.set_title(f"Omega Code: {title}\nCoherence = {coherence:.4f}", 
                 fontsize=14, fontweight='bold')
    ax.view_init(elev=20, azim=rotation_angle % 360)
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([-2, 2])
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"  ✓ Saved: {save_path}")
    
    plt.close()


def create_lifecycle_animation(
    coherence_history: list,
    emergent_time_history: list,
    output_path: str = "outputs/torus_lifecycle_animation.gif",
    frames_per_phase: int = 3,
) -> None:
    """
    Create animated GIF showing torus evolution through all three phases.
    
    Parameters:
      coherence_history: List of coherence values from lifecycle
      emergent_time_history: List of Ωτ values from lifecycle
      output_path: Path to save GIF
      frames_per_phase: Number of frames per phase transition
    """
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    # Collect frame data
    frames_data = []
    
    # Phase 1: Expansion (coherence = 1.0, slow rotation)
    print("  Rendering Phase 1: Expansion...")
    for i in range(frames_per_phase):
        rotation = (i / frames_per_phase) * 45  # Slow 45° rotation
        frames_data.append({
            'coherence': 1.0,
            'interference': 0.3,
            'rotation': rotation,
            'phase': 'Phase 1: Expansion (Coherence = 1.0000)',
        })
    
    # Phase 2: The Fall (coherence decreases, faster rotation, more noise)
    print("  Rendering Phase 2: The Fall...")
    num_fall_frames = len(coherence_history)
    for i, coherence in enumerate(coherence_history):
        rotation = 45 + (i / num_fall_frames) * 135  # 45° to 180°
        # Interference amplitude increases as coherence drops
        interference = 1.0 + (1.0 - coherence) * 2.0
        frames_data.append({
            'coherence': coherence,
            'interference': interference,
            'rotation': rotation,
            'phase': f'Phase 2: The Fall (Coherence = {coherence:.4f})',
        })
    
    # Phase 3: The Great Work (coherence recovers, smooth rotation)
    print("  Rendering Phase 3: The Great Work...")
    num_alchemy_frames = len(emergent_time_history)
    # Simulate recovery of coherence during alchemy
    for i in range(num_alchemy_frames):
        progress = i / num_alchemy_frames
        # Start from end of fall, recover toward higher coherence
        recovered_coherence = coherence_history[-1] + progress * (0.9 - coherence_history[-1])
        rotation = 180 + (progress * 135)  # 180° to 315°
        interference = 1.0 + (1.0 - recovered_coherence) * 1.5
        frames_data.append({
            'coherence': recovered_coherence,
            'interference': interference,
            'rotation': rotation,
            'phase': f'Phase 3: The Great Work (Coherence = {recovered_coherence:.4f})',
        })
    
    # Render animation
    def update_frame(frame_idx):
        ax.clear()
        data = frames_data[frame_idx]
        
        X, Y, Z, C = create_torus_frame(
            coherence=data['coherence'],
            interference_amplitude=data['interference'],
            rotation_angle=data['rotation'],
        )
        
        surf = ax.plot_surface(X, Y, Z, facecolors=cm.get_cmap('RdYlBu_r')(C),
                               rstride=1, cstride=1, shade=False, alpha=0.9)
        
        ax.set_xlabel("X (Manifestation)")
        ax.set_ylabel("Y (Manifestation)")
        ax.set_zlabel("Z (Consciousness)")
        ax.set_title(f"Omega Code (Ω): {data['phase']}", fontsize=12, fontweight='bold')
        ax.view_init(elev=20, azim=data['rotation'])
        ax.set_xlim([-4, 4])
        ax.set_ylim([-4, 4])
        ax.set_zlim([-2, 2])
    
    print(f"  Creating animation with {len(frames_data)} frames...")
    anim = FuncAnimation(fig, update_frame, frames=len(frames_data), 
                         interval=100, repeat=True)
    
    # Save as GIF
    writer = PillowWriter(fps=10)
    anim.save(output_path, writer=writer)
    print(f"  ✓ Animation saved: {output_path}")
    plt.close()


def render_phase_snapshots(
    coherence_history: list,
    output_dir: str = "outputs",
) -> None:
    """
    Render static snapshots at key lifecycle points.
    
    Parameters:
      coherence_history: List of coherence values
      output_dir: Directory to save images
    """
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n  Rendering phase snapshots...")
    
    # Phase 1: Pre-fall (perfect coherence)
    render_torus_snapshot(
        coherence=1.0,
        interference_amplitude=0.3,
        rotation_angle=0.0,
        title="Phase 1: Expansion (Perfect Unity)",
        save_path=f"{output_dir}/torus_phase1_expansion.png",
    )
    
    # Phase 2: Mid-fall (decoherence peak)
    mid_fall_idx = len(coherence_history) // 2
    mid_fall_coherence = coherence_history[mid_fall_idx]
    render_torus_snapshot(
        coherence=mid_fall_coherence,
        interference_amplitude=2.0,
        rotation_angle=90.0,
        title=f"Phase 2: The Fall (Decoherence Peak)",
        save_path=f"{output_dir}/torus_phase2_fall.png",
    )
    
    # Phase 3: Post-fall (partial recovery)
    final_coherence = coherence_history[-1]
    recovered_coherence = final_coherence + 0.2  # Assume partial recovery
    render_torus_snapshot(
        coherence=recovered_coherence,
        interference_amplitude=1.0,
        rotation_angle=180.0,
        title="Phase 3: The Great Work (Alchemy Underway)",
        save_path=f"{output_dir}/torus_phase3_alchemy.png",
    )


if __name__ == "__main__":
    print("\n" + "="*70)
    print("  TORUS FLOW VISUALIZATION: Lifecycle Animation")
    print("="*70 + "\n")
    
    # Example usage: create sample coherence/time histories
    num_fall_steps = 30
    coherence_fall = [1.0 - (i / num_fall_steps) ** 1.5 * 0.35 for i in range(num_fall_steps)]
    emergent_time_fall = [0.1 * i for i in range(num_fall_steps)]
    
    # Render snapshots
    render_phase_snapshots(coherence_fall)
    
    # Create animation
    create_lifecycle_animation(coherence_fall, emergent_time_fall)
    
    print("\n✓ Torus visualization complete!")
