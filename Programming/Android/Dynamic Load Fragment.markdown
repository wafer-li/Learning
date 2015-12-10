# Dynamic Load Fragment

Tags: Android

[TOC]

---



## 1) Get the `FragmentManager` 

- When in activity, just invoke the `getFragmentManager()` method
- When in Fragment, use `getChildFragmentManager()` to get the `FragmentManager` 


```java
//when in the activity
FragmentManager fragmentManager = getFragmentManager();

//when in the fragment
FragmentManager fragmentManager = getActivity().getFragmentManager();
```

## 2) Invoke `beginTransaction()` to start a Transaction

> This method is belong to the **FragemntManager**

```java
FragmentTransaction transcation = fragmentManager.beginTransaction();

```

## 3) Add Fragment to the container, usually, use the `replace()` method to achieve {#add}

> The difference between `add()` and `replace()`
If you invoke the `addToBackStack()` method, they both add the Fragment to the back stack,

> - The `replace()` remove the existing fragment and adds a new fragment.
    - There is just one Layout.
    - It will reinstante the Fragment.
- The `add()` method just add an instance to to the backstack, and retain the existing fragments. 
    - There will be 2 Layouts.
    - It won't reinstante the Fragment, **ONLY IF** it **doesn't be recycled** by the system.
- When to use `add()` and `replace()`
    - Basically, they both act the same effect, so to prevent the Layout redundancy, use `replace()`
    - But, if you need to start the AsyncTask or another Thread in the lifecycle of Fragment, the reinstantiation of using `place()` will cost lots of resources, use `add()` by another way instead.
    
```java
/**
* This way aims at resolve the following problem
* 1. The reinstantiaiton of Fragment
* 2. The Layout redundancy of multiple Fragment
*/

//Check the Fragment isAdded. Aim to #1 
public void switchContent(Fragment from, Fragment to) {

    // The mContent is the current fragment
    if (mContent != to) {
        mContent = to;
        FragmentTransaction transaction = mFragmentMan.beginTransaction().setCustomAnimations(
                android.R.anim.fade_in, R.anim.slide_out);
        if (!to.isAdded()) {    // Judge if is added
        
            // if not added, hide the current Fragment and add the next to Activity
            transaction.hide(from).add(R.id.content_frame, to).commit(); 
        } else {
            //if added, just show the next.
            transaction.hide(from).show(to).commit(); 
        }
    }
}

//Check the saveInstance to avoid the activity reinstance. Aim to #2
@Override
protected void onCreate (Bundle savedInstanceState) {
    if (savedInstanceState == null) {
        getFragmentManager().beginTransaction().add(android.R.id.content,
            new UIFragment(),"Tag").commit();
    } else {
        //if the instance does be recover,
        //use `findFragmentByTag()` to find the reference of the Fragment
          UIFragment fragment1 = getFragmentManager().findFragmentById(R.id.fragment1);
          UIFragment fragment2 = getFragmentManager().findFragmentByTag("tag");
          UIFragment fragment3 = ...
          ...
          //show one of them
          getFragmentManager().beginTransaction()
          .show(fragment1)
          .hide(fragment2)
          .hide(fragment3)
          .hide(...)
          .commit();
    }
}
```

## 4) One more step, the Fragment Management

> In this section, we face the two vivid situation 

### 1. Return to specific stack {#return-to-root}
> When we open a lot of Fragments, and we want to return to the root. Use the [popBackStack()](http://developer.android.com/reference/android/app/FragmentManager.html) to pop the Fragment upper than the specific one

###2. Switch between Fragments

- Using the `add() show() hide()` method()
    > The same as using `FragmentPagerAdapter`

    > - Just show and hide specific Fragment, do nto enter the Fragment lifecycle
    > - When hide, the Fragment is active, and will cause the Touch Event leak to the lower Fragment

- Using the `replace()` method 
    > The same as using `FragmentStatePagerAdapter`
    >    - Avoid the Touch Event leak, and reduce the management cost
    >    - But it will enter the lifecycle of Fragment, and whatever the `addToBackStack()` is invoked, the `onCreateView()` will **always be invoked**. If you need to load data from **Internet**, it will cost a lot(may be)

- Which is better?
    - If there is a lot of cost of Fragment management, compare to the cost of link to the Internet, the cost of managerment seems to more costly, choose `replace()`
    - If you do need to access large number of the Internet source, than choose the `add(), show(), hide()` method, if so, you need to be headache of the management.
    
###3. What should be cautious when using the `add(), show(), hide()` method

- When you are in an Fragment, use `getChildFragmentManager()` instead of `getFragmentManager()` in activity

- Do **not reinstante** the Fragment, and aware of the **redundancy of the Fragment Layout**.
> See [The previous node](#add) for more information

- Retrun to the root Fragment
> See [here](#return-to-root)

- Catch the Touch Event to prevent leaking to lower Fragment

    - Set the upper Fragment layout `clickable`
        ```xml
        <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:clickable="true" />
        ```
    
    - Do the catch in java
        
        ```java
@Override
public View onCreateView(LayoutInflater inflater,ViewGroup container,Bundle savedInstance){
            View root;
            
             /*here is an implementation*/
             
              root.setOnTouchListener(new View.OnTouchListener() {
                public boolean onTouch(View v, MotionEvent event) {
                    return true;
                    }
    });
    return root;
}

        ```


