RECOVERED FLIGHT CONTROLLER -- FIRMWARE IMAGE
=============================================

A small UAV was recovered after loss of link. Its flight-controller
flash was dumped to `uav_recovery.fw`. The board runs a Lacuna
Microsystems LCM-16 core. The authentication token we need is checked
on-device; it is never printed to the logs.

Recover the token. It is the flag, in the form Intern_Pro_Max{...}.

Note: the flash contains plenty of leftover strings from manufacturing
and telemetry. Most of them are junk. Only the token the core actually
accepts is correct, and you get a limited number of submissions.
