# RecyclerView

Tags: Android

[TOC]

---

## 1) Basic Usage

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

## 2) Add a OnItemClickListener
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



