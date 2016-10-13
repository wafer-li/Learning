# AsyncTask with Callback

Tags: Android

`AsyncTask` 和回调的结合使用
一般用于此 Task 被高度复用的情况，否则一般作为 `Activity` 的内部类实现

[TOC]

---

## 1. 定义一个用于回调的接口

```java
public interface TaskListener {
    void onResult(Object result);
}
```

## 2. 添加 Listener 作为 Task 的类成员
```java
class Task extends AsyncTask<Void,Void,Object> {

    private TaskListener taskListener;

    public void setListener(TaskListener taskListener) {
        this.taskListener = taskListener;
    }
}
```

## 3.通过接口成员调用其方法

> 为保证线程安全，应该在 Task 的 `onPostExecute()` 方法中完成该操作

```java
protected Object onPostExecute(Object result) {
    taskListener.onResult(result);
}
```

## 4. Activity 实现该接口处理回调数据

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