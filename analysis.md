System :
    - products
    - accounts [activation:email]
    - orders , track order
    -coupons
    -payment
    -dashboard
--------------------------
    -celery , redis
    -caching
    -optmization
    -django command
    -translation
    -ajax
    -docker
    -deploy [heroku - aws]
----------------------------
    -API
    -Docs
----------------------------
Products :
    - name
    - sku
    - brand    * [name-img]
    - images   *
    - subtitle (light_description)
    - description
    - tags     * package
    - price
    - flag [new-sale-feature] dropdown
    - quantity
    - reviews  * [user_id-product_id-rate[0:5]-feedback ,datetime]
    - category * [name,img]

Order :
    - status [recieved, processed, shipped,delivered]
    - id
    - total items
    - delivery time
    - order time
    - total
    - sub_total

OrderDetail :
    - order_id
    - product_id
    - price
    - quantity
    - total

user :
    - address *
    - name
    - email
    - image
    - phone_number *
--------------------------------------
    - reusable apps
    - single apps
    - 3s