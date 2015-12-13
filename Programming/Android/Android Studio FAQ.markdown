# Android Studio FAQ

Tags: Android

---

## 1. .gitignore

> If you want to stay away from merge conflicts, please do not directly use the Android Studio's default `.gitignore`, but add some modifitions

> There some good modifitions

1. The `/.idea` folder
> The `/.idea` folder will be automatically generate by the Gradle.
When add new dependencies, the build process will add the description of the dependencies into the files inside the `./idea` folder. So it will cause conflict easily.
**So, do remenber to ignore it.**

2. The `.iml` files
> The `.iml` files will be automatically generate by Gradle, when you import the gradle format projects.
As the same reason, it will add some description into the `.iml` files.
**So, ignore it.**

3. The `/gradle.properties` file
> This file often **only** contain the **proxy** of the gradle.
But when you using the Android Studio, it will ask you to **import the proxy settings of Android Studio** as the proxy of gradle, when you click the gradle sync button.
**So, if your crew are using different proxy settings, do ignore it.**

4. Supplement: Don't forget to `git rm` the stuff you ignore

So, there is my `.gitignore`, only works in `Android Studio`

```.gitignore
*.iml
/.idea
/gradle.properties
.gradle
/local.properties
.DS_Store
/build
/captures
```

## 2. When cannot resolve symbols

> Firstly, you need to check if the dependencies were added correctly, if that doesn't help.

> Please follow the instructions:

1. Check the `gradle` settings, which is in the `Settings` layout 
2. Delete the local repo, **reclone** it from remote
3. Try click the `Gradle Sync` button
4. Build -> Clean the project
5. Build -> Rebuild the project

> And remenber, when you finish cloning, using the `Open existing Project` or `Import from gradle` rather than click it in the `recently projects`

## 3. When cannot recongnize module

> If your Android Studio cannot recongnize your moudule, such as `app` and other modules.
In the Build menu, it's just a few items

![Poisonous](http://ww2.sinaimg.cn/large/8c1fca6bjw1eyyb1dvnnmj20zk0qotb3.jpg)

<span style="font-size:1.5em;font-weight:bold">
Backup your repo into the remote repository, and reclone it.
When the clone is finished, rebuild the project
</span>

