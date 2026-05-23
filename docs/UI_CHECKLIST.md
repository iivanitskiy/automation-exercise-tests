# UI Checklist — Automation Exercise

Источник: [Test Cases](https://automationexercise.com/test_cases)

| TC | Сценарий | Приоритет | Автотест | Статус |
|----|----------|-----------|----------|--------|
| 1 | Register User | P0 | `test_case_01_register_user` | ✅ |
| 2 | Login (correct credentials) | P0 | `test_case_02_login_with_correct_credentials` | ✅ |
| 3 | Login (incorrect credentials) | P1 | `test_case_03_login_with_incorrect_credentials` | ✅ |
| 4 | Logout User | P1 | `test_case_04_logout_user` | ✅ |
| 5 | Register with existing email | P1 | `test_case_05_register_with_existing_email` | ✅ |
| 6 | Contact Us Form | P2 | `test_case_06_contact_us_form` | ✅ |
| 7 | Verify Test Cases Page | P2 | `test_case_07_verify_test_cases_page` | ✅ |
| 8 | All Products + Product Detail | P0 | `test_case_08_verify_all_products_and_detail` | ✅ |
| 9 | Search Product | P0 | `test_case_09_search_product` | ✅ |
| 10 | Subscription (Home) | P1 | `test_case_10_subscription_on_home_page` | ✅ |
| 11 | Subscription (Cart) | P2 | `test_case_11_subscription_on_cart_page` | ✅ |
| 12 | Add Products in Cart | P0 | `test_case_12_add_products_in_cart` | ✅ |
| 13 | Product quantity in Cart | P1 | `test_case_13_verify_product_quantity_in_cart` | ✅ |
| 14 | Place Order: Register while Checkout | P1 | — | 📋 Backlog |
| 15 | Place Order: Register before Checkout | P0 | `test_case_15_place_order_register_before_checkout` | ✅ |
| 16 | Place Order: Login before Checkout | P1 | — | 📋 Backlog |
| 17 | Remove Products From Cart | P1 | `test_case_17_remove_products_from_cart` | ✅ |
| 18 | View Category Products | P2 | `test_case_18_view_category_products` | ✅ |
| 19 | View & Cart Brand Products | P2 | `test_case_19_view_brand_products` | ✅ |
| 20 | Search + Cart after Login | P2 | — | 📋 Backlog |
| 21 | Add review on product | P2 | `test_case_21_add_review_on_product` | ✅ |
| 22 | Add to cart (Recommended) | P2 | `test_case_22_add_to_cart_from_recommended` | ✅ |
| 23 | Address details in checkout | P2 | — | 📋 Backlog |
| 24 | Download Invoice | P2 | — | 📋 Backlog |
| 25 | Scroll Up (Arrow button) | P3 | `test_case_25_scroll_up_with_arrow` | ✅ |
| 26 | Scroll Up (without Arrow) | P3 | `test_case_26_scroll_up_without_arrow` | ✅ |

## Покрытие

- **Автоматизировано:** 22 из 26 UI сценариев (~85%)
- **Backlog:** TC 14, 16, 20, 23, 24 (checkout-варианты, invoice, cart persistence)

## Запуск

```bash
# Smoke UI
pytest tests/ui -m smoke

# Все UI
pytest tests/ui -m ui
```
