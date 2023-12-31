# PHP
## Data Type
- Primitive types <small><sup>[***[PHP Manual 10/29/2022](https://www.php.net/manual/en/language.types.intro.php)***]<sup></small>
    - Scalar Types
        - Numbers
            - [Integer](datatype-integer.php)
            - [Float](datatype-float.php)(Double)
        - [Boolean](datatype-boolean.php)
        - [String](datatype-string.php)
            - [Read more about strings](string/README.md)
    - Compound Types
        - [Array](datatype-array.php)
            - [Read more about arrays](array/README.md)
        - [Object](datatype-object.php)
        - [Callable](datatype-callable.php)
        - [Iterable](datatype-iterable.php)
    - Special Types
        - [Resource](datatype-resource.php)
        - [NULL](datatype-null.php)
- Type Checking <small><sup>[***[PHP Manual 10/29/2022](https://www.php.net/manual/en/function.gettype.php)***]<sup></small>
    - [`get_class()`](typecheck-get-class.php)
    - [**`gettype()`**](typecheck-get-type.php)
    - [**`settype()`**](typecheck-set-type.php)
    - [**`is_int()`**](typecheck-is-int.php)
    - [**`is_string()`**](typecheck-is-string.php)
    - [`is_resource()`](typecheck-is-resource.php)
    - [`is_scalar()`](typecheck-is-scalar.php)
    - [`is_float()`](typecheck-is-float.php)
    - [`is_null()`](typecheck-is-null.php)
    - [**`is_numeric()`**](typecheck-is-numeric.php)
    - [`is_object()`](typecheck-is-object.php)
    - [`is_array()`](typecheck-is-array.php)
    - [`is_bool()`](typecheck-is-bool.php)
    - [`is_callable()`](typecheck-is-callable.php)
    - [`function_exists()`](typecheck-is-func-exists.php)
    - [`method_exists()`](typecheck-is-method-exists.php)
    - [`get_debug_type()`](typecheck-get-debug-type.php)
        - Gets the type name of a variable in a way that is suitable for debugging <small><sup>[***[PHP Manual 10/29/2022](https://www.php.net/manual/en/function.get-debug-type.php)***]<sup></small>
        - This is for ***PHP 8***
    - [`is_nan()`](typecheck-is-nan.php)
    - [`is_finite()`](typecheck-is-nan.php)
    - [`is_infinite()`](typecheck-is-nan.php)
- Type Cast
    - [**`String to int`**](typecast-str-to-int.php)
    - [**`Float to int`**](typecast-float-to-int.php)
