# 🧩 neo Morphe patches

Morphe patch bundle for the `neo` Android app (`com.cbt.neodigital`).

## ❓ About

This project contains a patch that disables neo's Developer options check. The separate USB debugging check is not changed.

### How to use these patches

Add this repository to Morphe Manager: https://github.com/rw00/neo-patch

<a href="https://morphe.software/add-source?github=rw00/neo-patch">
  <img src=".github/assets/add-to-morphe.svg" alt="Add to Morphe" height="48">
</a>

## 🩹 Patches list

<!-- PATCHES_START EXPANDED -->
> **[v1.0.0-dev.1](https://github.com/rw00/neo-patch/releases/tag/v1.0.0-dev.1)**&nbsp;&nbsp;•&nbsp;&nbsp;`dev`&nbsp;&nbsp;•&nbsp;&nbsp;1 patches total
<details open>
<summary>📦 neo&nbsp;&nbsp;•&nbsp;&nbsp;1 patch</summary>
<br>

**Package name:** `com.cbt.neodigital`

| 💊&nbsp;Patch | 📜&nbsp;Description | ⚙️&nbsp;Options |
|----------|----------------|-----------|
| [Disable Developer options check](#disable-developer-options-check) | Allows the app to run with Developer options enabled. |  |

</details>

<!-- PATCHES_END -->

### 🛠️ Building locally

- Run `./gradlew buildAndroid`
- The built patches .mpp file is found in `patches/build/libs/patches-*.mpp`
- Patch the mpp file using [Morphe-Desktop](https://github.com/MorpheApp/morphe-desktop)
  like any other patch bundle.

See the [Morphe documentation](https://github.com/MorpheApp/morphe-documentation) for more information.

## 📜 License

neo Patches are licensed under the [GNU General Public License v3.0](LICENSE)
