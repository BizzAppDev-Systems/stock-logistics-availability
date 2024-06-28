def migrate(cr, version):
    # Requête pour vérifier l'existence des clés spécifiques dans la table `ir_config_parameter`
    cr.execute(
        """SELECT id, key FROM ir_config_parameter
        WHERE key IN ('stock_available.stock_available_mrp_based_on', 'stock_available_mrp_based_on')"""
    )
    records = cr.fetchall()

    for record in records:
        # Insérer un enregistrement correspondant dans la table `ir_model_data`
        query = """INSERT INTO ir_model_data (
            name,
            model,
            module,
            res_id,
            noupdate)
            VALUES (
                'default_stock_available_mrp_based_on',
                'ir.config_parameter',
                'stock_available_mrp',
                %s,
                True)"""
        cr.execute(query, (record[0],))

        # Mettre à jour la clé de l'enregistrement trouvé
        cr.execute(
            """UPDATE ir_config_parameter
            SET key = 'stock_available_mrp.stock_available_mrp_based_on'
            WHERE id = %s""",
            (record[0],)
        )

