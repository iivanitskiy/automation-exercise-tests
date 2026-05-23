# API Checklist — Automation Exercise

Источник: [APIs List](https://automationexercise.com/api_list)

| # | Сценарий | Method | Endpoint | Ожидаемый код | Автотест |
|---|----------|--------|----------|---------------|----------|
| 1 | Get All Products List | GET | `/api/productsList` | 200 + список products | `test_api_01_get_all_products_list` |
| 2 | POST To All Products List | POST | `/api/productsList` | 405 + unsupported method | `test_api_02_post_to_all_products_list_not_supported` |
| 3 | Get All Brands List | GET | `/api/brandsList` | 200 + список brands | `test_api_03_get_all_brands_list` |
| 4 | PUT To All Brands List | PUT | `/api/brandsList` | 405 + unsupported method | `test_api_04_put_to_all_brands_list_not_supported` |
| 5 | POST To Search Product | POST | `/api/searchProduct` | 200 + products (param: search_product) | `test_api_05_post_search_product` |
| 6 | POST Search without parameter | POST | `/api/searchProduct` | 400 + missing param message | `test_api_06_post_search_product_missing_parameter` |
| 7 | Verify Login (valid) | POST | `/api/verifyLogin` | 200 + User exists! | `test_api_07_verify_login_valid_details` |
| 8 | Verify Login (no email) | POST | `/api/verifyLogin` | 400 + missing param message | `test_api_08_verify_login_missing_email` |
| 9 | DELETE Verify Login | DELETE | `/api/verifyLogin` | 405 + unsupported method | `test_api_09_delete_verify_login_not_supported` |
| 10 | Verify Login (invalid) | POST | `/api/verifyLogin` | 404 + User not found! | `test_api_10_verify_login_invalid_details` |
| 11 | Create User Account | POST | `/api/createAccount` | 201 + User created! | `test_api_11_create_user_account` |
| 12 | Delete User Account | DELETE | `/api/deleteAccount` | 200 + Account deleted! | `test_api_12_delete_user_account` |
| 13 | Update User Account | PUT | `/api/updateAccount` | 200 + User updated! | `test_api_13_update_user_account` |
| 14 | Get User Detail by email | GET | `/api/getUserDetailByEmail` | 200 + user JSON | `test_api_14_get_user_detail_by_email` |

## Параметры API 11–14 (create/update)

`name`, `email`, `password`, `title`, `birth_date`, `birth_month`, `birth_year`, `firstname`, `lastname`, `company`, `address1`, `address2`, `country`, `zipcode`, `state`, `city`, `mobile_number`

## Запуск только API

```bash
pytest tests/api -m api
```
