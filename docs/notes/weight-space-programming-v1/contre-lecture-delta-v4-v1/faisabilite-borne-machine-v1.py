# Faisabilité de la borne propre de la machine (v4) : plafonds consignés, jamais les durées réelles.
H_STOCK = 324.0  # création le 5 novembre 12:00 UTC -> 19 novembre 00:00 UTC
def duree(deja, p, s, h_rest):  # depense.duree_max_minutes
    libre = 40 - deja - h_rest * s
    return int(max(0.0, min(1440, 0.9 * libre / p * 60)))
for p in (0.3, 0.5, 0.8):
    for s in (0.022, 0.05):
        for n, cm in ((14, 25), (18, 25)):
            fab = duree(0, p, s, H_STOCK)
            cons = fab; t = 6.0; ok_copies = 0
            for k in range(n):
                t += 2.0
                borne = cons / 60 * p + t * s
                m = duree(borne, p, s, H_STOCK - t)
                if m < cm + 5: break
                cons += cm + 5; ok_copies += 1
            t += 2.0
            borne = cons / 60 * p + t * s
            mc = duree(borne, p, s, H_STOCK - t)
            reel = 6 * p + n * 0.5 * p + 4 * p + H_STOCK * s
            print(f"carte {p} stockage {s} copies {n}: fabrication plafonnée {fab} min ({fab/60*p:.1f} USD imputés) ; "
                  f"copies admises {ok_copies}/{n} ; causal {mc} min -> {'admis' if mc >= 60 and ok_copies == n else 'REFUSÉ'} ; "
                  f"pire cas réel du devis {reel:.1f} USD")
