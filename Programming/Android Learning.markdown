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
    private List<Object> list;
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
- The @Override method usage
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
- Basically is to use a callback to achieve this

<span style="font-size:20px">
① Define a Listener interface(Often as a inner class of `Adapter`)
</span>
```java
public interface OnItemClickListener {
    void onItemClick (View view, int position);
}
```

② Add the interface to `Adapter`

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