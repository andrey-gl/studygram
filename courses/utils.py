def get_user_list(queryset):
    list_final = []
    for item in queryset:
        list_final.append(str(item.last_name) + str(item.first_name))
    return list_final
