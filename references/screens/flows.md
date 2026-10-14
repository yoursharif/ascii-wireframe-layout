# Flows

Multi-screen output: a flow, a journey or all screens of one feature. Follow the Multiple screens rules in `SKILL.md`.

Read `primitives.md` first, then the screen file for each width the flow uses. Each screen keeps its own width, so web and mobile screens can share one flow.

Two differences from a real reply or saved file, both so this file works as a reference:

- Screen headings here are `###` under the flow's `##`. In a reply or saved file they are `##` under the `#` title.
- Blocks here are labelled `wire` so the validator checks them. In a reply or saved file they are labelled `text`.

## Password reset, web to mobile

Password reset flow, 5 screens (2 web, 3 mobile).

Flow: Forgot password (web) > Check your email (web) > Reset email (phone) > Set new password (app) > Password updated (app)

### 1. Forgot password

Web app, 80 columns.

```wire
+------------------------------------------------------------------------------+
| LOGO  Acme                                                <Sign in>   <Help> |
+------------------------------------------------------------------------------+
|                                                                              |
|                 +------------------------------------------+                 |
|                 |                                          |                 |
|                 |          FORGOT YOUR PASSWORD?           |                 |
|                 |                                          |                 |
|                 | Enter the email you use for Acme and we  |                 |
|                 | will send you a link to reset it.        |                 |
|                 |                                          |                 |
|                 | Email                                    |                 |
|                 | +--------------------------------------+ |                 |
|                 | | sam@acme.com                         | |                 |
|                 | +--------------------------------------+ |                 |
|                 |                                          |                 |
|                 | [[          Send reset link           ]] |                 |
|                 |                                          |                 |
|                 |            <Back to sign in>             |                 |
|                 |                                          |                 |
|                 +------------------------------------------+                 |
|                                                                              |
| (c) 2026 Acme                                            <Privacy>   <Terms> |
+------------------------------------------------------------------------------+
```

Next: click [[ Send reset link ]] > 2. Check your email

### 2. Check your email

Web app, 80 columns.

```wire
+------------------------------------------------------------------------------+
| LOGO  Acme                                                <Sign in>   <Help> |
+------------------------------------------------------------------------------+
|                                                                              |
|                 +------------------------------------------+                 |
|                 |                                          |                 |
|                 |             CHECK YOUR EMAIL             |                 |
|                 |                                          |                 |
|                 | We sent a reset link to sam@acme.com.    |                 |
|                 | Open it on any device. The link expires  |                 |
|                 | in 30 minutes.                           |                 |
|                 |                                          |                 |
|                 | (i) Have the Acme app? The link opens    |                 |
|                 |     straight in the app on your phone.   |                 |
|                 |                                          |                 |
|                 | Didn't get it?  <Resend email>  (0:45)   |                 |
|                 |                                          |                 |
|                 |         <Use a different email>          |                 |
|                 |                                          |                 |
|                 +------------------------------------------+                 |
|                                                                              |
| (c) 2026 Acme                                            <Privacy>   <Terms> |
+------------------------------------------------------------------------------+
```

Next: user opens the email on their phone > 3. Reset email

### 3. Reset email

Mobile mail app, 40 columns.

```wire
+- Mail -------------------------------+
| 9:41                            100% |
| [<]  Inbox                     [...] |
|                                      |
| Reset your Acme password             |
| Acme <no-reply@acme.com>             |
| to me                    Today 10:02 |
| ------------------------------------ |
|                                      |
| Hi Sam,                              |
|                                      |
| We got a request to reset the        |
| password for your Acme account.      |
|                                      |
| [[         Reset password         ]] |
|                                      |
| This link expires in 30 minutes.     |
| If you didn't ask for this, you can  |
| ignore this email.                   |
|                                      |
| ------------------------------------ |
| <Reply>                    <Forward> |
+--------------------------------------+
```

Next: tap [[ Reset password ]], the link opens the Acme app > 4. Set new password

### 4. Set new password

Mobile app, 40 columns.

```wire
+- New password -----------------------+
| 9:41                            100% |
| [X]                                  |
|                                      |
| SET A NEW PASSWORD                   |
| For sam@acme.com                     |
|                                      |
| New password                         |
| +----------------------------------+ |
| | ************              <Show> | |
| +----------------------------------+ |
| Strength  [#######---]  Good         |
|                                      |
| Confirm new password                 |
| +----------------------------------+ |
| | ************              <Show> | |
| +----------------------------------+ |
|                                      |
| [x] At least 8 characters            |
| [x] One number or symbol             |
| [x] Passwords match                  |
|                                      |
| [ ] Sign out of all other devices    |
|                                      |
|                                      |
| ------------------------------------ |
| [[        Update password         ]] |
+--------------------------------------+
```

Next: tap [[ Update password ]] > 5. Password updated

### 5. Password updated

Mobile app, 40 columns.

```wire
+- Done -------------------------------+
| 9:41                            100% |
|                                      |
|                                      |
|           PASSWORD UPDATED           |
|                                      |
|   Your new password is set. Use it   |
|     next time you sign in on any     |
|               device.                |
|                                      |
| (i) We sent a confirmation email     |
|     to sam@acme.com.                 |
|                                      |
|                                      |
|                                      |
| ------------------------------------ |
| [[        Continue to Acme        ]] |
+--------------------------------------+
```
