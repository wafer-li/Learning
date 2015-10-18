#Android Learning
**Editor: Cmd Markdown**
Tags: Programming-Learning Anadroid

[TOC]
## Front-end
### 1. RecyclerView
#### 1) Basic Usage

<span style="font-size:20px">① Add dependencies</span>
```
compile 'com.android.support:recyclerview-v7:+'
```

<span style="font-size:20px">
② Add RecyclerView to `layout.xml` and define the `item_layout.xml`
</span>

- The RecyclerView
```xml
<android.support.v7.widget.RecyclerView
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:id="@+id/recycler"
    android:scrollbars="vertical"/>
    
    <!-- Must define the scrollbars attr -->
```

- The `item_layout.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent">

<TextView
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:id="@+id/quest_item" />

</LinearLayout>
```

<span style="font-size:20px">
③ Set the **LayoutManager** and **Adapter**
</span>
```java
@Override
public View onCreateView(LayoutInflater inflater, ViewGroup parent, Bundle savedInstanceState) {

    View v = inflater.inflate(R.layout.fragment_recyclerview, parent, false);

    //set the Recycler
    mRecyclerView = (RecyclerView) v.findViewById(R.id.recycler_view);
    
    //set LayoutManager
    mRecyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
    
    //DataSet
    mCrimes = CrimeLab.get(getActivity()).getCrimes();
    
    //set the Adapter
    mRecyclerView.setAdapter(new CrimeAdapter());

    return v;
}
```

<span style="font-size:20px">④ Define the **Adapter** and its **@Override** method</span>

- The Adapter contains **DataSet** and ***often*** a inner `ViewHolder`
```java
public class MyAdapter extends RecyclerView.Adapter<MyAdapter.ViewHolder> {
    
    //The DataSet
    private List<Object> mDatas;
    //...other stuff
    
    //The inner ViewHolder
    class MyViewHolder extends Recycler.ViewHolder {
        //The views
        public TextView textView;
        
        //The Ctor is Auto-Generate
        public MyViewHolder (View itemView) {
            super(itemView);
            //Just set the view as the @param is Ok
        }
    }
}
```
- The **@Override** method usage
```java
@Override
public MyViewHolder onCreateViewHolder(ViewGroup parent, int ViewType) {
    //TODO: Build a ViewHolder which is the inner class
    
    /**
    * Notice: The ViewType is use to build the diffirent ViewHolder
    * to display diffirent ViewHolder
    */
}

@Override
public void onBindViewHolder(MyViewHolder holder, int position) {
    //TODO: Bind the view with the DataSet
    //Just like the getView() method in ListView 
    //But it's more easier
}

public int getItemCount() {
    //TODO: return the amount of item
}
```

#### 2) Add a OnItemClickListener
- Basically is to use a callback method to achieve this
- Need to define a `<ripple>` drawable and set as the background of the View Widget to display the feedback

<span style="font-size:20px">
① Define a Listener interface(Often as a inner class of `Adapter`)
</span>
```java
public interface OnItemClickListener {

    /**
    * This is the callback method.
    * Aimed to notify the context the Click Event.
    * To modify UI, also need to pass the position for UI updating or do othertings
    */
    void onItemClick (View view, int position);
}
```

② Add the interface to `Adapter`
```java
class MyAdapter ... {
    private OnItemClickListener mOnItemClickListener;
    
    public void setOnItemClickListener(OnItemClickListener mOnItemClickListener) {
        this.mOnItemClickListener = mOnItemClickListener;
    }
}
```

③ Set the **original Listener** in `onBindViewHolder()` with `ViewHolder` and call the **callback method**
```java
public void onBindViewHolder (final MyViewHolder holder, final int position) {
    //Bind the View with Data
    holder.textView.setText(mDatas.get(position));
    
    //Set the Listener
    //Notice: if the callback was set, then set the Click Event for the ViewHolder
    if(mOnItemClickLitener != null) {
        holder.textView.setOnClickListener (new OnClickListener() {
            @Override
            public void onClick (View v) {
                int pos = holder.getLayoutPosition();
                //Call the callback method
                mOnItemClickListener.onItemClick(hodler.textView, pos);
            }
        });
    }
}
```
④ Do with the result in the context **(Fragment or Activity)**
```java
@Override
public void onCreateView(...) {
    mAdapter.setOnClickListener (new OnItemClickListener() {
        @Override
        public void onItemClick(View v, int position) {
            //Update UI or execute some operation
        }
    })
}
```

### 2. Splash Activity

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

### 3. Dynamic Load Fragment

#### 1) Get the `FragmentManager` 

- When in activity, just invoke the `getFragmentManager()` method
- When in Fragment, use `getChildFragmentManager()` to get the `FragmentManager` 


```java
//when in the activity
FragmentManager fragmentManager = getFragmentManager();

//when in the fragment
FragmentManager fragmentManager = getActivity().getFragmentManager();
```

#### 2) Invoke `beginTransaction()` to start a Transaction

> This method is belong to the **FragemntManager**

```java
FragmentTransaction transcation = fragmentManager.beginTransaction();

```

#### 3) Add Fragment to the container, usually, use the `replace()` method to achieve {#add}

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

#### 4) One more step, the Fragment Management

> In this section, we face the two vivid situation 

##### 1. Return to specific stack {#return-to-root}
> When we open a lot of Fragments, and we want to return to the root. Use the [popBackStack()](http://developer.android.com/reference/android/app/FragmentManager.html) to pop the Fragment upper than the specific one

#####2. Switch between Fragments

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
    
#####3. What should be cautious when using the `add(), show(), hide()` method

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

----
## Back-end
### 1. AsyncTask with Callback
1) Define a interface for callback
```java
public interface TaskListener {
    void onResult(Object result);
}
```
2) Add the Listener to the Task
```java
class Task extends AsyncTask<Void,Void,Object> {

    private TaskListener taskListener;

    public void setListener(TaskListener taskListener) {
        this.taskListener = taskListener;
    }
}
```
3) Call the listener's method in the **onPostExecute()** method
```java
protected Object onPostExecute(Object result) {
    taskListener.onResult(result);
}
```
4) Set Listener and do with the result in the **Mian Thread**
**Notice**

- Activity must implement the Listener you defined.
- The callback method onResult() is used to **update** UI.
    - With AdapterView, use `adapter.notifyDataSetChanged()` to **update** the UI
    
```java
public class MainTread extends Activity implement TaskListener{
    //your stuff
    Task task = new Task(this);
    task.execute();
    
    @Override
    public void onResult(Object result){
        //UPDATE YOUR UI HERE
    }
}
```