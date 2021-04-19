def get_user_list(queryset):
    list_final = []
    for item in queryset:
        list_final.append(
            {
                'id': str(item.id),
                'name': str(item.first_name),
                'surname': str(item.last_name)
            })
    return list_final
