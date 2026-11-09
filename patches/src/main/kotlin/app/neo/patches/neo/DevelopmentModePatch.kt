package app.neo.patches.neo

import app.morphe.patcher.patch.patch
import app.morphe.patcher.util.returnEarly
import app.neo.patches.shared.COMPATIBILITY_NEO

@Suppress("unused")
val disableDeveloperOptionsCheckPatch = patch(
    name = "Disable Developer options check",
    description = "Allows the app to run with Developer options enabled."
) {
    compatibleWith(COMPATIBILITY_NEO)

    execute {
        DevelopmentModeCheckFingerprint.method.returnEarly(false)
    }
}
