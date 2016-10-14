# Java Programming Items

Tags： Java

Base on *Effective Java Second Edition*
To improve my Java skills.

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Java Programming Items](#java-programming-items)  
&emsp;[1. Object construction & Destruction](#1-object-construction-destruction)  
&emsp;&emsp;[1.1 Using the static factory method primary to construct the object](#11-using-the-static-factory-method-primary-to-construct-the-object)  
&emsp;&emsp;[1.2 Using builder when meeting multiple constructor parma](#12-using-builder-when-meeting-multiple-constructor-parma)  

<!-- /MDTOC -->

---

## 1. Object construction & Destruction

### 1.1 Using the static factory method primary to construct the object

> Something must be made clear at the very beginning.
That is: **Using the static factory method does NOT mean that "We do not use the constructor"**
Sometimes, we do no need to use the constructor, but at most of time, we still need to use the constructor to assist.
And usually, when we **"only"** use the static factory, there is a **private** constructor method.

Pros:

1. The static factory method has **name**

    > The advantages are quite clear.
    With the name, we can make it more clear that what the properties of the object we constructed.
    And when we need the constructor **with the same sinature(The parma type) but have different effects**, the costructor can not afford this type of work, because we can only have one constructor with the specified parmas.
    The example is at following:

    ```java
    /**
    * This class is a ramdom int generator.
    * Its constructor receive two parmas, min and max,
    * and use this as the generated integers range.
    */
    public class RandomIntGenerator {
        private final int min;
        private final int max;

        /**
        * Notice that the min and max is final, and it's resonable.
        * Therefore, we need to assign it at the constructor just as follow
        * @parma min The range lo of the generated integers
        * @parma max The range hi of the generated integers
        */
        public RandomIntGenerator(int min, int max) {
            this.min = min;
            this.max = max;
        }

        /**
        * Notice the following static method, they all return the new Object of RandomIntGenerator
        * And because of their names,
        * we can construct different object by using the same method parma.
        */

        public static RandomIntGenerator between(int max, int min) {
            return new RandomIntGenerator(min, max);
        }

        public static RandomIntGenerator biggerThan(int min) {
            return new RandomIntGenerator(min, Integer.MAX_VALUE);
        }

        public static RandomIntGenerator smallerThan(int max) {
            return new RandomIntGenerator(Integer.MIN_VALUE, max);
        }

        public int next() {...}

    }
    ```

2. The static factory has no necessity to **construct NEW object every time**

    > When we using the immutable class, it's important to avoid constructing duplicate objects.

3. The static factory can return any subtype of the origin return type

    > That leads us to a point: We can get the object, but avoid making the class public.
    Therefore, this properties make the **interface-based framework** come into real.
    That is , we can create a **interface**, and make multiple class implement this interface, but the class has **non-public** assess control.
    And let our static factory **return the interface**, so we can get the object and no damage to the **non-public** class.
    The example is as follow:

    ```java
    public interface RandomGenerator<T> {
    // Create the interface
        T next();
    }

    /**
    * Notice that, the "real" generator are both *package assessable*
    * That is the two class is not public, so how do we get the instance of the two objects?
    *
    * Nope, we do not use the instance of the "class",
    * we could only use the instance of the "interface"
    * Because the interface is generics, it's more suitable to this situation.
    *
    * That is "interface-based framework",
    * the only thing which the client can get is the "interface",
    * we can do more things behind the scene,
    * and when we add a new high performance implementation of RandomIntGenerator,
    * we can only change the return statement of the static factory,
    * the new implementation will be automatically deployed into all clients.
    */

    // Implement the interface as the <Integer>
    class RandomIntGenerator implement RandomGenerator<Integer> {
        private final int min;
        private final int max;

        RandomIntGenerator(int min, int max) {
            this.min = min;
            this.max = max;
        }

        public Integer next() {...}
    }

    // Implement the interface as the <String>
    class RandomStringGenerator implements RandomGenerator<String> {
        private final String prefix;

        RandomStringGenerator(String prefix) {
            this.prefix = prefix;
        }

        public String next() {...}
    }

    // Invoke the tipical RamdonGenerator through static factory
    public final class RandomGenerators {
        // Suppresses default constructor, ensuring non-instantiability.
        private RandomGenerators() {}

        public static final RandomGenerator<Integer> getIntGenerator() {
            return new RandomIntGenerator(Integer.MIN_VALUE, Integer.MAX_VALUE);
        }

        public static final RandomGenerator<String> getStringGenerator() {
            return new RandomStringGenerator('');
        }
    }


    ```

4. Using the static factory could have more tidy code

    > Especially the generics code.
    By using the static factory, we can use the compiler to do the **type inference** clean the code.
    The example is as follow:

    ```java
    public static <K, V> HashMap<K, V> newInstance() {
        retrun new HashMap<K, V>();
    }
    // When not using the static factory
    Map<String, List<String>> m = new HashMap<String, List<String>>();

    // When using the static factory
    // The complier will do the job of match the generics parma
    Map<String, List<String>> m = HashMap.newInstance();
    ```

Cons:

1. If the class do not have the `public` or `protected` constructor, it cannot return the subclass of the origin return type.

    > Therefore, it leads to the composition(**复合**) rather than **inherition**

2. The static factory actually have no difference between the other static methods

    > Therefore, we use some special name to specify it as the static factory.
    Such as:

    > 1. `valueOf` -- The convertion between the value and its Object, often seen at the wrapper.
    > 2. `of` -- The other form of `valueOf`
    > 3. `getInstance` -- Return the instance of the class, but it can't be said it is definitely the **brand new** object.
    > 4. `newInstance` -- The only difference between the above is this method ensure the object is **brand new**
    > 5. `getType` -- Like `getInstance`, but use it when the static factory is at the different class, just the Pro 3 shows.
    > 6. `newType` -- Like `newInstance`, but use it when the static factory is at the different class, just the Pro 3 shows.


### 1.2 Using builder when meeting multiple constructor parma

> When the constructor has
