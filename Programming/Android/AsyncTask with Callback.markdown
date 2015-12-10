# AsyncTask with Callback

Tags: Android

[TOC]

---

## 1) Define a interface for callback
```java
public interface TaskListener {
    void onResult(Object result);
}
```
## 2) Add the Listener to the Task
```java
class Task extends AsyncTask<Void,Void,Object> {

    private TaskListener taskListener;

    public void setListener(TaskListener taskListener) {
        this.taskListener = taskListener;
    }
}
```
## 3) Call the listener's method in the `onPostExecute()` method
```java
protected Object onPostExecute(Object result) {
    taskListener.onResult(result);
}
```
## 4) Set Listener and do with the result in the `Mian Thread`
**Notice:**

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