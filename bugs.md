# U-Tube: Bugs & Glitches Log

Tracking document for reported bugs, glitches, their root causes, and resolutions.

---

## Bug #1: Navigation Bar Glitches (Top Bubble & Bottom Collapse Glitch)

### 1. Top Bar Glitch (Stray Shorts Lens Bubble Floating Over Top Bar)
- **Reported Behavior**:
  - Tapping tabs (specifically Shorts) caused a circular bubble containing the tab icon and label ("Shorts") to appear at the very top of the screen (`Y ≈ 0`), stuck over the top app bar / U-Tube branding.
- **Root Cause**:
  - `NavLens` (the iOS-inspired liquid-glass lens transition animation) computes its translation relative to `bar.getTop()` and `bar.getLeft()`.
  - When the bottom navbar was wrapped in `mobile_nav_cluster` (`LinearLayout`), `mobile_nav_glass.getTop()` became `0` (relative to the cluster).
  - `NavLens` was placed at `Y = 0` (top of screen).
  - Furthermore, `NavLens.stop()` never set `setVisibility(View.GONE)`, leaving the lens persistently floating on screen.
- **Fix**:
  - Disabled `playNavLens` in `MobileBrowseActivity` (tab switching is now instant, responsive, and seamless without jarring flying lens delays).
  - Patched `NavLens.place()` to dynamically walk up parent view hierarchies to correctly calculate absolute coordinates in the root layout.
  - Added `setVisibility(GONE)` to `NavLens.stop()` to guarantee no lingering visual artifacts.

---

### 2. Bottom Navigation Bar Glitch (Colored Gradient Blobs & Scroll Collapse Layout Corruption)
- **Reported Behavior**:
  - A bright cyan/teal radial gradient circle was painted across the right side of the bottom navigation bar, clipping the Account tab.
  - When scrolling down, the collapse animation attempted to shrink the navbar into bubbles, causing the `BottomNavigationView` menu items to jump, disappear, glitch text labels, and corrupt the view hierarchy.
- **Root Cause**:
  - `NavBloom`: Was attached as a background drawable to `mBottomNav`. It drew colored radial gradient blobs (`0xFF40C8E0` teal from previous search item IDs) directly onto the glass navbar canvas.
  - Destructive Item Hiding: `setNavCollapsed` was calling `item.setVisible(false)` on Material `BottomNavigationView` items while animating width on every frame. `BottomNavigationView` does not support real-time width resizing coupled with menu item visibility toggling; it triggers full asynchronous menu re-inflation and clears active item views.
- **Fix**:
  - Removed `NavBloom` attached drawable on `mBottomNav`, restoring the clean, transparent Wavelet liquid glass aesthetic.
  - Introduced a separate, dedicated `mobile_active_bubble` (56dp circular glass bubble) inside `mobile_nav_cluster`.
  - On scroll down, `mobile_nav_glass` (260dp capsule) smoothly cross-fades into `mobile_active_bubble` alongside `mobile_search_fab`, presenting two stable floating circular bubbles:
    `[ Active Tab Bubble (56dp) ]   [ Search Bubble (56dp) ]`
  - On scroll up or tap, `mobile_active_bubble` smoothly cross-fades back into the full capsule.
  - `BottomNavigationView` internal state is never mutated, eliminating all layout glitches and label jumping.
