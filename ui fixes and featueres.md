# U-Tube: UI Fixes & Features

Tracking document for UI enhancements, design refinements, and feature updates across U-Tube (v0.1+).

---

## 1. Player & Playback UI Fixes

- **Removed Circular Discs from Player Controls**:
  - Removed the dark tinted / circular glass background discs (`GlassDrawable.applyButton`) behind player buttons:
    - **Fullscreen** (`mobile_player_fullscreen`)
    - **Cast** (`mobile_player_cast`)
    - **CC / Subtitles** (`mobile_player_subtitles`)
    - **Lock & Unlock** (`mobile_player_lock`, `mobile_player_unlock`)
    - **Settings / More** (`mobile_player_more`)
    - **Audio Symbol** (`mobile_player_audio`)
  - All controls now render with clean, borderless icons (`?attr/selectableItemBackgroundBorderless`), ensuring a minimal and unobstructed viewing experience.
- **Removed Down Arrow Buttons & Redundant Functions**:
  - **Bottom-Right Down Arrow (`mobile_player_actions_toggle`)**: Completely removed along with the actions toggle function. The action buttons row (like, dislike, comments, etc.) stays cleanly visible and integrated under the seek bar in fullscreen without needing an extra down-chevron button.
  - **Top-Left Down Arrow (`mobile_player_back`)**: Completely removed along with the minimize-to-miniplayer action. Audio button margin is aligned starting directly at `8dp` and the player title margin is re-centered cleanly at `60dp`.
- **Dead & Unused Code Cleanup**:
  - Completely purged unused `mBackButton`, `mActionsToggle`, and `mActionsShown` Java fields, bindings, listeners, and references from `MobilePlaybackActivity.java`.
  - Removed obsolete `mobile_player_back` and `mobile_player_actions_toggle` View tags from `activity_mobile_playback.xml`.
  - Deleted unused `ic_player_minimize.xml` drawable asset and unreferenced string resources (`mobile_player_hide_actions`, `mobile_player_show_actions`).
- **Removed Timeline Center Pop-up & Fly-back Animation**:
  - Previously, double-tap seek or scrubbing caused a large glass pill (`mobile_player_seek_time`) displaying `position / duration` to fly from the bottom corner into the center of the video frame, hover there, and fly back down upon animation completion.
  - **Fix**: Removed the center pop-up and fly-in/fly-out translation animations completely. The timestamp and progress position remain anchored cleanly at the bottom of the video, preserving an unobstructed video viewing experience with no distracting animations.
- **Disabled Mini-Player**:
  - Removed unwanted floating mini-player bar overlays on video exit/fold to keep layout clean and intuitive.
- **Double-Tap Fast Seek**:
  - Fast-forward (`+10`) and rewind overlay indicators remain responsive on lateral screen edges while keeping the center unobstructed.

---

## 2. Navigation Bar & Glass Styling (Wavelet Redesign)

- **Liquid Glass Navigation Cluster**:
  - Floating centered horizontal capsule with real-time backdrop blur.
  - High-precision glass styling with configurable liquid refraction and subtle border tints.
- **Updated Navigation Tabs**:
  - **Home**: `ic_nav_home` ("Home")
  - **Shorts** (Replaced *Explore*): `ic_nav_shorts` ("Shorts")
  - **Account** (Replaced *Library*): `ic_nav_you` ("Account")
  - **Search**: Standalone 56dp circular floating glass button with `ic_mobile_search`.
- **Wavelet Scroll Collapse Behavior**:
  - **Scroll Down**: Navbar smoothly contracts into two floating circular bubbles centered horizontally at the bottom:
    `[ Active Tab Bubble (e.g. Home) ]  [ Search Bubble ]`
  - **Scroll Up / Tap**: Expands smoothly back to the full pill displaying Home, Shorts, and Account with labels.

---

## 3. Branding, Package & Architecture

- **App Name & Versioning**:
  - Rebranded universally to **U-Tube** (`v0.1`).
  - Package ID: `com.utube` (debug package `com.utube.debug`).
- **Icons & Visual Identity**:
  - Red liquid-glass YouTube play icon applied to all adaptive and monochrome launcher mipmaps.
- **MeeTune Complete Removal**:
  - Removed all MeeTune references, packages, and code couplings.
- **Upstream & Repository Integration**:
  - App updates point directly to `https://github.com/ajaykumarreddy-k/U-tube`.
  - Music & external audio redirection points to `https://github.com/ajaykumarreddy-k/Wavelet`.

---

## 4. Planned & In-Progress Improvements

- [ ] Further fine-tuning of player gesture overlays (brightness/volume indicators).
- [ ] Customizable theme accents matching Android 13+ dynamic Monet theming.
- [ ] Refined landscape and tablet layouts for the floating navigation cluster.

