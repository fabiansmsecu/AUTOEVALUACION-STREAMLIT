rubricas = {
    'Gestión de Acceso': {
        '¿Existen políticas y procedimientos documentados para la gestión de accesos?': {
            1: {
                'descripcion': 'No se tienen políticas ni procedimientos documentados.',
                'recomendacion': 'Diseñar e implementar políticas básicas de gestión de accesos y capacitar al personal.'
            },
            2: {
                'descripcion': 'Existen políticas y procedimientos, pero no están completamente documentados.',
                'recomendacion': 'Completar la documentación existente y definir responsables claros.'
            },
            3: {
                'descripcion': 'Políticas y procedimientos documentados y regularmente revisados.',
                'recomendacion': 'Mantener el proceso de revisión periódica y actualizar según cambios regulatorios.'
            },
            4: {
                'descripcion': 'Cumplen con todos los requisitos establecidos por ISO 27001.',
                'recomendacion': 'Continuar con auditorías internas y evidenciar cumplimiento para auditorías externas.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Explorar soluciones avanzadas como IAM basado en inteligencia artificial.'
            }
        },
        '¿Se implementan controles de autenticación fuertes para acceder a sistemas críticos?': {
            1: {
                'descripcion': 'No se implementan controles de autenticación.',
                'recomendacion': 'Implementar controles básicos como contraseñas robustas o autenticación de doble factor.'
            },
            2: {
                'descripcion': 'Se implementan controles de autenticación de manera limitada o inconsistente.',
                'recomendacion': 'Estandarizar el uso de autenticación fuerte en todos los sistemas críticos.'
            },
            3: {
                'descripcion': 'Controles de autenticación fuertes implementados de manera regular.',
                'recomendacion': 'Ampliar cobertura a usuarios remotos y dispositivos móviles.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de autenticación de ISO 27001.',
                'recomendacion': 'Mantener políticas actualizadas y realizar pruebas de seguridad periódicas.'
            },
            5: {
                'descripcion': 'Implementación avanzada de controles de autenticación que supera los requisitos estándar.',
                'recomendacion': 'Explorar tecnologías como biometría o autenticación sin contraseña.'
            }
        }
    },
    'Seguridad Física y Ambiental': {
        '¿Existen medidas de seguridad física para proteger los equipos críticos del departamento de sistemas?': {
            1: {
                'descripcion': 'No hay medidas de seguridad física implementadas.',
                'recomendacion': 'Instalar cerraduras, controles de acceso físico y monitoreo básico.'
            },
            2: {
                'descripcion': 'Medidas de seguridad física parciales o insuficientes.',
                'recomendacion': 'Completar las medidas físicas faltantes y asignar responsables de seguridad.'
            },
            3: {
                'descripcion': 'Medidas de seguridad física implementadas regularmente.',
                'recomendacion': 'Revisar anualmente la eficacia de las medidas implementadas.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de seguridad física de ISO 27001.',
                'recomendacion': 'Mantener controles actuales y preparar evidencias para auditorías.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Integrar sistemas avanzados como CCTV inteligente o controles biométricos.'
            }
        },
        '¿Se realizan controles ambientales para proteger la infraestructura tecnológica (temperatura, humedad, etc.)?': {
            1: {
                'descripcion': 'No se realizan controles ambientales.',
                'recomendacion': 'Implementar sensores básicos de temperatura y humedad en salas críticas.'
            },
            2: {
                'descripcion': 'Controles ambientales realizados de manera irregular o insuficiente.',
                'recomendacion': 'Establecer monitoreo continuo y definir umbrales de alerta.'
            },
            3: {
                'descripcion': 'Controles ambientales implementados regularmente.',
                'recomendacion': 'Mantener registros y realizar mantenimientos preventivos.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de controles ambientales de ISO 27001.',
                'recomendacion': 'Continuar con mantenimiento preventivo y auditorías periódicas.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Incorporar sistemas inteligentes de control ambiental integrados con alarmas tempranas.'
            }
        }
    },
    'Gestión de Comunicaciones y Operaciones': {
        '¿Se utilizan procedimientos seguros para la transmisión de datos sensibles dentro y fuera de la organización?': {
            1: {
                'descripcion': 'No se utilizan procedimientos seguros para la transmisión de datos.',
                'recomendacion': 'Establecer políticas básicas de cifrado para correos y archivos sensibles.'
            },
            2: {
                'descripcion': 'Procedimientos seguros utilizados de manera parcial o inconsistente.',
                'recomendacion': 'Definir procedimientos claros y capacitar al personal en su uso.'
            },
            3: {
                'descripcion': 'Procedimientos seguros utilizados regularmente.',
                'recomendacion': 'Ampliar controles a todos los canales de comunicación, incluidos dispositivos móviles.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de seguridad de transmisión de datos de ISO 27001.',
                'recomendacion': 'Realizar pruebas periódicas de seguridad en los canales de transmisión.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Implementar cifrado de extremo a extremo y monitoreo de tráfico cifrado.'
            }
        },
        '¿Se realizan pruebas periódicas de vulnerabilidades y evaluaciones de riesgos en la infraestructura de redes?': {
            1: {
                'descripcion': 'No se realizan pruebas de vulnerabilidades ni evaluaciones de riesgos.',
                'recomendacion': 'Contratar una evaluación inicial de vulnerabilidades por un tercero.'
            },
            2: {
                'descripcion': 'Pruebas de vulnerabilidades realizadas de manera limitada o irregular.',
                'recomendacion': 'Establecer un calendario regular de pruebas y definir responsables.'
            },
            3: {
                'descripcion': 'Pruebas de vulnerabilidades y evaluaciones de riesgos realizadas regularmente.',
                'recomendacion': 'Documentar hallazgos y crear planes de remediación con plazos definidos.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de pruebas y evaluaciones de ISO 27001.',
                'recomendacion': 'Continuar con pruebas periódicas e incluir auditorías externas cada cierto tiempo.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Integrar herramientas automáticas de escaneo continuo y monitoreo en tiempo real.'
            }
        }
    },
    'Control de Acceso a la Información': {
        '¿Se implementan controles para limitar el acceso a la información confidencial y crítica dentro del departamento de sistemas?': {
            1: {
                'descripcion': 'No se implementan controles de acceso a la información.',
                'recomendacion': 'Definir políticas mínimas de control de acceso y restringir el acceso a personal autorizado.'
            },
            2: {
                'descripcion': 'Controles de acceso implementados de manera limitada o inconsistente.',
                'recomendacion': 'Establecer perfiles de acceso basados en roles y revisarlos periódicamente.'
            },
            3: {
                'descripcion': 'Controles de acceso implementados regularmente.',
                'recomendacion': 'Incluir revisiones semestrales de permisos y auditorías internas.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de control de acceso de ISO 27001.',
                'recomendacion': 'Mantener controles y pruebas periódicas de acceso.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Aplicar control de acceso granular y soluciones Zero Trust.'
            }
        },
        '¿Se establecen y mantienen políticas para la clasificación y etiquetado de la información dentro del departamento de sistemas?': {
            1: {
                'descripcion': 'No se establecen ni mantienen políticas para clasificación y etiquetado.',
                'recomendacion': 'Crear políticas básicas para identificar datos confidenciales y críticos.'
            },
            2: {
                'descripcion': 'Políticas de clasificación y etiquetado establecidas pero no mantenidas adecuadamente.',
                'recomendacion': 'Actualizar políticas y capacitar al personal sobre su aplicación.'
            },
            3: {
                'descripcion': 'Políticas de clasificación y etiquetado mantenidas regularmente.',
                'recomendacion': 'Auditar la aplicación de las políticas y reforzar controles.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de clasificación y etiquetado de ISO 27001.',
                'recomendacion': 'Continuar con auditorías periódicas y mejorar la documentación de procesos.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Integrar herramientas automáticas de Data Loss Prevention (DLP) para la clasificación de datos.'
            }
        }
    },
    'Gestión de Incidentes de Seguridad de la Información': {
        '¿Existe un procedimiento documentado para la gestión de incidentes de seguridad de la información?': {
            1: {
                'descripcion': 'No hay procedimiento documentado para la gestión de incidentes.',
                'recomendacion': 'Diseñar e implementar procedimientos básicos de respuesta a incidentes.'
            },
            2: {
                'descripcion': 'Procedimiento documentado pero no actualizado o implementado de manera limitada.',
                'recomendacion': 'Actualizar el procedimiento y capacitar al personal sobre su aplicación.'
            },
            3: {
                'descripcion': 'Procedimiento documentado y regularmente revisado e implementado.',
                'recomendacion': 'Realizar simulacros periódicos y documentar resultados.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de gestión de incidentes de ISO 27001.',
                'recomendacion': 'Mantener la práctica actual y evidenciar cumplimiento.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Incorporar simulaciones avanzadas (red teaming) y herramientas de orquestación SOAR.'
            }
        },
        '¿Se realiza capacitación y simulacros periódicos para el personal sobre cómo responder a incidentes de seguridad de la información?': {
            1: {
                'descripcion': 'No se realizan capacitaciones ni simulacros sobre incidentes de seguridad.',
                'recomendacion': 'Establecer programas básicos de capacitación para todo el personal.'
            },
            2: {
                'descripcion': 'Capacitaciones y simulacros realizados de manera irregular o insuficiente.',
                'recomendacion': 'Definir un calendario anual obligatorio de capacitaciones y simulacros.'
            },
            3: {
                'descripcion': 'Capacitaciones y simulacros realizados regularmente.',
                'recomendacion': 'Evaluar la eficacia de las capacitaciones mediante mediciones.'
            },
            4: {
                'descripcion': 'Cumple totalmente con los requisitos de capacitación y simulacros de ISO 27001.',
                'recomendacion': 'Mantener las actividades actuales y mejorar contenido basado en incidentes recientes.'
            },
            5: {
                'descripcion': 'Implementación avanzada que supera los requisitos estándar.',
                'recomendacion': 'Integrar ejercicios complejos como war games y pruebas en tiempo real.'
            }
        }
    }
}
