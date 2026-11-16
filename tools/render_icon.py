"""Draw the themed-icon (Android 13+ monochrome) layer: the U-Tube play badge.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / "mobile" / "src" / "stmobile" / "res"

VECTOR_CONTENT = """<?xml version="1.0" encoding="utf-8"?>
<!-- U-Tube: themed-icon (Android 13+) monochrome mark - YouTube play badge -->
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path
        android:fillColor="#FFFFFF"
        android:fillType="evenOdd"
        android:pathData="M34,32 C27.37,32 22,37.37 22,44 L22,64 C22,70.63 27.37,76 34,76 L74,76 C80.63,76 86,70.63 86,64 L86,44 C86,37.37 80.63,32 74,32 Z M48,46.5 L48,61.5 Q48,63.5 49.7,62.5 L62.5,55 Q64.2,54 62.5,53 L49.7,45.5 Q48,44.5 48,46.5 Z" />
</vector>
"""

if __name__ == "__main__":
    (RES / "drawable" / "ic_launcher_monochrome.xml").write_text(VECTOR_CONTENT, encoding="utf-8")
    print("ok")
