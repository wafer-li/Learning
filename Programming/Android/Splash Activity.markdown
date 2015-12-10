### Splash Activity

Tags: Android

---


- Display a short splash, use for the background loading.

> Usually, use the AsyncTask to do the background loadling. 

- Use the `Handler.postDelayed()` method to show an delay

``` java
new Handler().postDelayed(new Runnable() {
            public void run() {
            goHome();
            }
            }, SPLASH_DELAY_MILLIS);
}
```
> Sometimes, the background loading might be fast, in this case, using a delay to avoid the screen flash.

- Set as the **LANCHER** activity
- Remember to use `finish()` method to **FINISH** the current activity




